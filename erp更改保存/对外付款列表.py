#对外付款列表 /sales/remit/payout/list      lvID:1710
def payout_list(request):
    '''
    描述： 对外付款列表
    模型： Payout
    作者： Zhl 2019-08-14
    '''
    EVENT_RIGHT = 1710

    try:
        Mine = request.session['mine_object']
        Mine.reload()
    except:
        Mine = MineManager()

    opera = Mine.auth(EVENT_RIGHT)
    if type(opera) == type(''):
        return HttpResponse(opera)
    try:
        # opera.remove(opera[1])
        opera.append({'depict': '导入', 'gateway': '/sales/remit/payout/imp', 'attr': ' id=page-opera:10:1990','descript': '', 'click': ' class="disabled"', 'parame': ''})
        # opera.append({'depict': '付款', 'gateway': '/sales/remit/payout/dopay?id=', 'attr': ' id=page-opera:11:1711','descript': '', 'click': ' class="disabled"', 'parame': ''})
        opera.append({'depict': '取消', 'gateway': '/sales/remit/payout/del?id=', 'attr': ' id=page-opera:13:1990','descript': '', 'click': ' class="disabled"', 'parame': ''})
        opera.append({'depict': '详情', 'gateway': '/sales/remit/payout/info?id=', 'attr': ' id=page-opera:11:1711','descript': '', 'click': ' class="disabled"', 'parame': ''})
    except:
        pass

    serach = {}
    ###权限验证结束###
    keystime = request.GET.get('keystime', '')
    #如果获取的值不为日期格式为空值
    serach['keystime'] = str(keystime)[:10]
    keyetime = request.GET.get('keyetime', '')
    #如果获取的值不为日期格式为空值
    serach['keyetime'] = str(keyetime)[:10]
    keytitle = request.GET.get('keytitle', '').strip()
    serach['keytitle'] = keytitle
    unit_list = Mine.Unit.get_unit_list()
    querys = Payout.objects.filter(status=200, un_id__in=unit_list)
    if keytitle != '':
        querys = querys.filter(Q(c_id__name__icontains = keytitle)|Q(title__icontains = keytitle))
    if keystime != '':
        querys = querys.filter(pay_time__gte = '%s 00:00:00' % keystime)
    if keyetime != '':
        querys = querys.filter(pay_time__lte = '%s 23:59:59' % keyetime)
    querys = querys.order_by('dostatus','-addtime')
    context={
        'opera': opera,
        'querys': querys,
        'serach': serach,
    }
    return render_to_response('payout_list.html', context, context_instance = RequestContext(request))
