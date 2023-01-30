import research_log_02

def main():

    logger_001 = research_log_02.create_logger_101()
    logger_001.debug("debug")
    logger_001.info("info")
    logger_001.error("erro")
    logger_001.warning("warning")

if __name__ == '__main__':
    main()
