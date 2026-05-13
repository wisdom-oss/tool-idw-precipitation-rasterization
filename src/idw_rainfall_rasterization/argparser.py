from argparse import ArgumentParser, BooleanOptionalAction, Namespace

__base_parser: ArgumentParser = ArgumentParser("idw-rainfall-rasterization")


def parse_cli_arguments() -> Namespace:
    """
    Parse the provided command line arguments and return the result

    :return: Parsed command line arguments
    :rtype: Namespace
    """

    __base_parser.add_argument(
        "--source",
        help="The source the precipitation data is taken from",
        choices=["file", "api"],
        default="api",
    )

    __base_parser.add_argument(
        "--save-netcdf",
        help="Save the generated rasterization as netCDF file for further usages",
        action=BooleanOptionalAction,
    )

    __base_parser.add_argument(
        "--output",
        help="The path to the output folder which will contain the image series, and optionally the cross-validation results and the NetCDF file for the rasterization",
        default="./output",
        metavar="path"
    )

    __base_parser.add_argument(
        "--cross-validation",
        help="Enable/Disable crossvalidation before the data is rasterized. Disabled per default",
        default=False,
        action=BooleanOptionalAction,
    )

    __base_parser.add_argument(
        "--rasterize",
        help="Enable/Disable rasterization of the data. Enabled by default",
        default=True,
        action=BooleanOptionalAction,
    )

    __base_parser.add_argument(
        "boundary_shape",
        help="A Shapefile defining the outer borders of the generated raster images and used stations",
    )

    args = __base_parser.parse_args()
    if args.source == "api":
        return args

    # as the file source needs some more arguments to be usable we now extend the
    # parser and add more
    return parse_file_loader_arguments()


def parse_file_loader_arguments() -> Namespace:
    """
    Extend the :data:`__base_parser` to also read in the arguments for the station
    list and the rainfall data.

    :return: The parsed command line arguments for handling the file source type
    :rtype: Namespace
    """

    __base_parser.add_argument(
        "dwd_station_list",
        help="The official station list of the dwd. This is used to determine which stations are inside of the supplied boundary. Optional if the source is set to 'api'",
    )
    return __base_parser.parse_args()
