import research_log

def main():

    logger_001 = research_log.create_logger_001()
    logger_001.info('test')

    logger_002 = research_log.create_logger_002()
    logger_002.info('test')


if __name__ == '__main__':
    main()
