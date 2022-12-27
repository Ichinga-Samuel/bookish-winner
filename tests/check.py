import logging

logger = logging.getLogger()

def mainc():
    print(mainc)
    logger.critical("Something Went Wrong %(one)s", extra={'one': 'pone', 'two': 'pny'})

def fun():
    logging.error(f"How you do{fun}", extra={'one': 'poi', 'two': 'opp'})


