import logging
import coloredlogs
from idw_rainfall_rasterization.argparser import parse_cli_arguments
from idw_rainfall_rasterization.enums import Datasource

def main() -> None:
    logger = logging.getLogger(__name__)
    coloredlogs.install(level="DEBUG", fmt="%(asctime)s %(levelname)s %(message)s")
    arguments = parse_cli_arguments()
    
    if not arguments.cross_validation and not arguments.rasterize:
        logger.critical("Please enable at least one of the tools functions.\nCross Validation:\tDisabled\nRasterization:\t\tDisabled")
        exit(1)

    match arguments.source:
        case Datasource.API:
            logger.info("Loading station data and precipitation data from the DWD Open Data Portal")
        case Datasource.FILES:
            if arguments.station_list is None:
                logger.critical("File-based generation selected but no station list provided")
                exit(1)
            if arguments.rainfall_data_dir is None:
                logger.critical("File-based generation selected but no rainfall data dir provided")
                exit(1)
            logger.info("Loading station data and precipitation data from locally available files")
        case _:
            logger.critical("Unknown datasource selected: %s", arguments.source)
            exit(1)
