# -*- coding: utf-8 -*-


def caiyun_reply(data):
    message = u'抱歉，发生未知错误。'
    status = data.get('status')
    if status == 'ok':
        message = data.get('summary', '')
    elif status == 'failed':
        error_type = data.get('error_type')
        if error_type == 'too_old':
            message = u'抱歉，因为数据延迟超过30分钟，不能提供天气信息。'
        elif error_type == 'too_sparse':
            message = u'抱歉，因为数据缺失，不能提供天气信息。'
        elif error_type == 'outside_station':
            message = u'抱歉，你所查询的位置，不在雷达站范围内。'
        elif error_type == 'no_latlon':
            message = u'抱歉，你所查询的位置，缺少经纬度参数。'
    return message


def caiyun_coord_reply(data):
    lat, lon = None, None
    status = data.get('status')
    if status == 'ok':
        coord = data.get('coord')
        lat = coord.get('lat')
        lon = coord.get('lng')
    return lat, lon
