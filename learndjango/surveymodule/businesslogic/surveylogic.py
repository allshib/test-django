





def parseparams(params):
    try:
        return [float(num) for num in params.strip('[]').split(',')]
    except:
        return None