# coding=utf-8
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class TbBaseparam(models.Model):
    paramid = models.CharField(db_column='ParamId', primary_key=True, max_length=40)  # Field name made lowercase.
    paramname = models.CharField(db_column='ParamName', max_length=256)  # Field name made lowercase.
    paramvalue = models.CharField(db_column='ParamValue', max_length=256)  # Field name made lowercase.
    paramtype = models.IntegerField(db_column='ParamType')  # Field name made lowercase.
    paramstatus = models.IntegerField(db_column='ParamStatus')  # Field name made lowercase.
    parammemo = models.CharField(db_column='ParamMemo', max_length=256, blank=True,
                                 null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_baseparam'


class TbDevicectrl(models.Model):
    controlid = models.CharField(db_column='ControlId', primary_key=True, max_length=40)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceId', max_length=40)  # Field name made lowercase.
    sequence = models.IntegerField(db_column='Sequence')  # Field name made lowercase.
    ctrlname = models.CharField(db_column='CtrlName', max_length=256)  # Field name made lowercase.
    control = models.IntegerField(db_column='Control')  # Field name made lowercase.
    ctrlchan = models.IntegerField(db_column='CtrlChan')  # Field name made lowercase.
    ctrlmemo = models.CharField(db_column='CtrlMemo', max_length=1024, blank=True,
                                null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_devicectrl'


class TbDeviceparam(models.Model):
    paramid = models.CharField(db_column='ParamId', primary_key=True, max_length=40)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceId', max_length=40, blank=True,
                                null=True)  # Field name made lowercase.
    paramname = models.CharField(db_column='ParamName', max_length=256)  # Field name made lowercase.
    paramalias = models.CharField(db_column='ParamAlias', max_length=256)  # Field name made lowercase.
    paramunit = models.CharField(db_column='ParamUnit', max_length=256, blank=True,
                                 null=True)  # Field name made lowercase.
    sequence = models.IntegerField(db_column='Sequence')  # Field name made lowercase.
    paramtype = models.IntegerField(db_column='ParamType')  # Field name made lowercase.
    arming = models.IntegerField(db_column='Arming')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    alarm = models.IntegerField(db_column='Alarm')  # Field name made lowercase.
    paramvalue = models.DecimalField(db_column='ParamValue', max_digits=20,
                                     decimal_places=6)  # Field name made lowercase.
    lowervalue = models.DecimalField(db_column='LowerValue', max_digits=20,
                                     decimal_places=6)  # Field name made lowercase.
    loweralarm = models.CharField(db_column='LowerAlarm', max_length=256, blank=True,
                                  null=True)  # Field name made lowercase.
    uppervalue = models.DecimalField(db_column='UpperValue', max_digits=20,
                                     decimal_places=6)  # Field name made lowercase.
    upperalarm = models.CharField(db_column='UpperAlarm', max_length=256, blank=True,
                                  null=True)  # Field name made lowercase.
    parammemo = models.CharField(db_column='ParamMemo', max_length=1024, blank=True,
                                 null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_deviceparam'


class TbDevicetype(models.Model):
    typeid = models.CharField(db_column='TypeId', primary_key=True, max_length=40)  # Field name made lowercase.
    catlog = models.IntegerField(db_column='CatLog')  # Field name made lowercase.
    catlogname = models.CharField(db_column='CatLogName', max_length=256)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    typename = models.CharField(db_column='TypeName', max_length=256)  # Field name made lowercase.
    vender = models.CharField(db_column='Vender', max_length=256)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=256)  # Field name made lowercase.
    module = models.CharField(db_column='Module', max_length=256, blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=1024, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_devicetype'


class TdAlarminfo(models.Model):
    alarmid = models.CharField(db_column='AlarmId', primary_key=True, max_length=40)  # Field name made lowercase.
    alarmtime = models.CharField(db_column='AlarmTime', max_length=40)  # Field name made lowercase.
    parentid = models.CharField(db_column='ParentId', max_length=40)  # Field name made lowercase.
    parentname = models.CharField(db_column='ParentName', max_length=256)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceId', max_length=40)  # Field name made lowercase.
    devicename = models.CharField(db_column='DeviceName', max_length=256)  # Field name made lowercase.
    paramid = models.CharField(db_column='ParamId', max_length=40)  # Field name made lowercase.
    paramname = models.CharField(db_column='ParamName', max_length=255)  # Field name made lowercase.
    alarmtype = models.IntegerField(db_column='AlarmType')  # Field name made lowercase.
    alarminfo = models.CharField(db_column='AlarmInfo', max_length=1024)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'td_alarminfo'


class TdAlarmperson(models.Model):
    personid = models.CharField(db_column='PersonId', primary_key=True, max_length=40)  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=256)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=40, blank=True, null=True)  # Field name made lowercase.
    telphone = models.CharField(db_column='Telphone', max_length=40, blank=True,
                                null=True)  # Field name made lowercase.
    mail = models.CharField(db_column='Mail', max_length=256, blank=True, null=True)  # Field name made lowercase.
    duty = models.IntegerField(db_column='Duty')  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'td_alarmperson'


class TdDevicealarm(models.Model):
    alarmid = models.CharField(db_column='AlarmId', primary_key=True, max_length=40)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceId', max_length=40)  # Field name made lowercase.
    devicename = models.CharField(db_column='DeviceName', max_length=256)  # Field name made lowercase.
    alarmcontent = models.CharField(db_column='AlarmContent', max_length=1024)  # Field name made lowercase.
    reserved = models.CharField(db_column='Reserved', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'td_devicealarm'


class TdDevicectrl(models.Model):
    controlid = models.CharField(db_column='ControlId', primary_key=True, max_length=40)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceId', max_length=40)  # Field name made lowercase.
    sequence = models.IntegerField(db_column='Sequence')  # Field name made lowercase.
    ctrlname = models.CharField(db_column='CtrlName', max_length=256)  # Field name made lowercase.
    control = models.IntegerField(db_column='Control')  # Field name made lowercase.
    ctrlchan = models.IntegerField(db_column='CtrlChan')  # Field name made lowercase.
    ctrlmemo = models.CharField(db_column='CtrlMemo', max_length=1024, blank=True,
                                null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'td_devicectrl'


class TdDeviceinfo(models.Model):
    deviceid = models.CharField(db_column='DeviceId', primary_key=True, max_length=40)  # Field name made lowercase.
    devicename = models.CharField(db_column='DeviceName', max_length=256)  # Field name made lowercase.
    parentid = models.CharField(db_column='ParentId', max_length=40, blank=True,
                                null=True)  # Field name made lowercase.
    parentname = models.CharField(db_column='ParentName', max_length=256, blank=True,
                                  null=True)  # Field name made lowercase.
    devtype = models.CharField(db_column='DevType', max_length=40, blank=True, null=True)  # Field name made lowercase.
    modulename = models.CharField(db_column='ModuleName', max_length=256, blank=True,
                                  null=True)  # Field name made lowercase.
    devno = models.CharField(db_column='DevNo', max_length=10)  # Field name made lowercase.
    devicetype = models.IntegerField(db_column='DeviceType')  # Field name made lowercase.
    devstatus = models.IntegerField(db_column='DevStatus')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    commmode = models.IntegerField(db_column='CommMode')  # Field name made lowercase.
    commport = models.CharField(db_column='CommPort', max_length=256, blank=True,
                                null=True)  # Field name made lowercase.
    deviceip = models.CharField(db_column='DeviceIP', max_length=256, blank=True,
                                null=True)  # Field name made lowercase.
    deviceport = models.IntegerField(db_column='DevicePort')  # Field name made lowercase.
    devuser = models.CharField(db_column='DevUser', max_length=256, blank=True, null=True)  # Field name made lowercase.
    devpsw = models.CharField(db_column='DevPsw', max_length=256, blank=True, null=True)  # Field name made lowercase.
    commaddr = models.IntegerField(db_column='CommAddr')  # Field name made lowercase.
    baudrate = models.IntegerField(db_column='BaudRate')  # Field name made lowercase.
    extdevid = models.CharField(db_column='ExtDevId', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    extparamid = models.CharField(db_column='ExtParamId', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase.
    duty = models.IntegerField(db_column='Duty')  # Field name made lowercase.
    armingstart = models.IntegerField(db_column='ArmingStart')  # Field name made lowercase.
    armingstop = models.IntegerField(db_column='ArmingStop')  # Field name made lowercase.
    posx = models.IntegerField(db_column='PosX')  # Field name made lowercase.
    posy = models.IntegerField(db_column='PosY')  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=256, blank=True,
                                null=True)  # Field name made lowercase.
    reserved = models.CharField(db_column='Reserved', max_length=1024, blank=True,
                                null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'td_deviceinfo'


class TdDeviceinfoTmp(models.Model):
    deviceid = models.CharField(db_column='DeviceId', primary_key=True, max_length=40)  # Field name made lowercase.
    devicename = models.CharField(db_column='DeviceName', max_length=256)  # Field name made lowercase.
    parentid = models.CharField(db_column='ParentId', max_length=40, blank=True,
                                null=True)  # Field name made lowercase.
    parentname = models.CharField(db_column='ParentName', max_length=256, blank=True,
                                  null=True)  # Field name made lowercase.
    devtype = models.CharField(db_column='DevType', max_length=40, blank=True, null=True)  # Field name made lowercase.
    modulename = models.CharField(db_column='ModuleName', max_length=256, blank=True,
                                  null=True)  # Field name made lowercase.
    devno = models.CharField(db_column='DevNo', max_length=10)  # Field name made lowercase.
    devicetype = models.IntegerField(db_column='DeviceType')  # Field name made lowercase.
    devstatus = models.IntegerField(db_column='DevStatus')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    commmode = models.IntegerField(db_column='CommMode')  # Field name made lowercase.
    commport = models.CharField(db_column='CommPort', max_length=256, blank=True,
                                null=True)  # Field name made lowercase.
    deviceip = models.CharField(db_column='DeviceIP', max_length=256, blank=True,
                                null=True)  # Field name made lowercase.
    deviceport = models.IntegerField(db_column='DevicePort')  # Field name made lowercase.
    devuser = models.CharField(db_column='DevUser', max_length=256, blank=True, null=True)  # Field name made lowercase.
    devpsw = models.CharField(db_column='DevPsw', max_length=256, blank=True, null=True)  # Field name made lowercase.
    commaddr = models.IntegerField(db_column='CommAddr')  # Field name made lowercase.
    baudrate = models.IntegerField(db_column='BaudRate')  # Field name made lowercase.
    extdevid = models.CharField(db_column='ExtDevId', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    extparamid = models.CharField(db_column='ExtParamId', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase.
    duty = models.IntegerField(db_column='Duty')  # Field name made lowercase.
    armingstart = models.IntegerField(db_column='ArmingStart')  # Field name made lowercase.
    armingstop = models.IntegerField(db_column='ArmingStop')  # Field name made lowercase.
    posx = models.IntegerField(db_column='PosX')  # Field name made lowercase.
    posy = models.IntegerField(db_column='PosY')  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=256, blank=True,
                                null=True)  # Field name made lowercase.
    reserved = models.CharField(db_column='Reserved', max_length=1024, blank=True,
                                null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'td_deviceinfo_tmp'


class TdDeviceparam(models.Model):
    paramid = models.CharField(db_column='ParamId', primary_key=True, max_length=40)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceId', max_length=40, blank=True,
                                null=True)  # Field name made lowercase.
    paramname = models.CharField(db_column='ParamName', max_length=256)  # Field name made lowercase.
    paramalias = models.CharField(db_column='ParamAlias', max_length=256)  # Field name made lowercase.
    paramunit = models.CharField(db_column='ParamUnit', max_length=256, blank=True,
                                 null=True)  # Field name made lowercase.
    sequence = models.IntegerField(db_column='Sequence')  # Field name made lowercase.
    paramtype = models.IntegerField(db_column='ParamType')  # Field name made lowercase.
    arming = models.IntegerField(db_column='Arming')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    alarm = models.IntegerField(db_column='Alarm')  # Field name made lowercase.
    paramvalue = models.DecimalField(db_column='ParamValue', max_digits=20,
                                     decimal_places=6)  # Field name made lowercase.
    lowervalue = models.DecimalField(db_column='LowerValue', max_digits=20,
                                     decimal_places=6)  # Field name made lowercase.
    loweralarm = models.CharField(db_column='LowerAlarm', max_length=256, blank=True,
                                  null=True)  # Field name made lowercase.
    uppervalue = models.DecimalField(db_column='UpperValue', max_digits=20,
                                     decimal_places=6)  # Field name made lowercase.
    upperalarm = models.CharField(db_column='UpperAlarm', max_length=256, blank=True,
                                  null=True)  # Field name made lowercase.
    parammemo = models.CharField(db_column='ParamMemo', max_length=1024, blank=True,
                                 null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'td_deviceparam'


class TdDictionary(models.Model):
    dictid = models.CharField(db_column='DictId', primary_key=True, max_length=40)  # Field name made lowercase.
    dicttype = models.CharField(db_column='DictType', max_length=255)  # Field name made lowercase.
    dictkey = models.CharField(db_column='DictKey', max_length=255)  # Field name made lowercase.
    dictvalue = models.CharField(db_column='DictValue', max_length=255)  # Field name made lowercase.
    reserved = models.CharField(db_column='Reserved', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'td_dictionary'


class TdGuardarea(models.Model):
    areaid = models.CharField(db_column='AreaId', primary_key=True, max_length=40)  # Field name made lowercase.
    areaname = models.CharField(db_column='AreaName', max_length=256)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceId', max_length=40)  # Field name made lowercase.
    parentid = models.CharField(db_column='ParentId', max_length=40)  # Field name made lowercase.
    linewidth = models.IntegerField(db_column='LineWidth')  # Field name made lowercase.
    label = models.CharField(db_column='Label', max_length=255, blank=True, null=True)  # Field name made lowercase.
    line = models.CharField(db_column='Line', max_length=2048, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'td_guardarea'


class TdPlatimage(models.Model):
    imageid = models.CharField(db_column='ImageId', primary_key=True, max_length=40)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceId', max_length=40)  # Field name made lowercase.
    imagetype = models.IntegerField(db_column='ImageType')  # Field name made lowercase.
    imgtype = models.IntegerField(db_column='ImgType')  # Field name made lowercase.
    imagelength = models.IntegerField(db_column='ImageLength')  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=256, blank=True, null=True)  # Field name made lowercase.
    image = models.TextField(db_column='Image', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'td_platimage'


class TdPlatlog(models.Model):
    logid = models.CharField(db_column='LogId', primary_key=True, max_length=40)  # Field name made lowercase.
    logtime = models.CharField(db_column='LogTime', max_length=40)  # Field name made lowercase.
    platname = models.CharField(db_column='PlatName', max_length=256)  # Field name made lowercase.
    logtype = models.IntegerField(db_column='LogType')  # Field name made lowercase.
    loglevel = models.IntegerField(db_column='LogLevel')  # Field name made lowercase.
    loginfo = models.CharField(db_column='LogInfo', max_length=1024)  # Field name made lowercase.
    reserved = models.CharField(db_column='Reserved', max_length=256, blank=True,
                                null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'td_platlog'


class TdPlatuser(models.Model):
    userid = models.CharField(db_column='UserId', primary_key=True, max_length=40)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=256)  # Field name made lowercase.
    userpsw = models.CharField(db_column='UserPsw', max_length=256, blank=True, null=True)  # Field name made lowercase.
    userright = models.IntegerField(db_column='UserRight')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'td_platuser'


class TdVideochannel(models.Model):
    channelid = models.CharField(db_column='ChannelId', primary_key=True, max_length=40)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceId', max_length=40)  # Field name made lowercase.
    vender = models.IntegerField(db_column='Vender')  # Field name made lowercase.
    channelname = models.CharField(db_column='ChannelName', max_length=256)  # Field name made lowercase.
    channel = models.IntegerField(db_column='Channel')  # Field name made lowercase.
    sequence = models.IntegerField(db_column='Sequence')  # Field name made lowercase.
    posx = models.IntegerField(db_column='PosX')  # Field name made lowercase.
    posy = models.IntegerField(db_column='PosY')  # Field name made lowercase.
    memo = models.CharField(db_column='Memo', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'td_videochannel'


class TdVideoshow(models.Model):
    showid = models.CharField(db_column='ShowId', primary_key=True, max_length=40)  # Field name made lowercase.
    videoid = models.CharField(db_column='VideoId', max_length=40)  # Field name made lowercase.
    vender = models.IntegerField(db_column='Vender', blank=True, null=True)  # Field name made lowercase.
    videoip = models.CharField(db_column='VideoIP', max_length=40, blank=True, null=True)  # Field name made lowercase.
    videochann = models.IntegerField(db_column='VideoChann', blank=True, null=True)  # Field name made lowercase.
    videouser = models.CharField(db_column='VideoUser', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase.
    videopsw = models.CharField(db_column='VideoPsw', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    videochannel = models.CharField(db_column='VideoChannel', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    sequence = models.IntegerField(db_column='Sequence', blank=True, null=True)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceId', max_length=40, blank=True,
                                null=True)  # Field name made lowercase.
    paramid = models.CharField(db_column='ParamId', max_length=40)  # Field name made lowercase.
    param = models.CharField(db_column='Param', max_length=255, blank=True, null=True)  # Field name made lowercase.
    showtext = models.CharField(db_column='ShowText', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    posx = models.IntegerField(db_column='PosX', blank=True, null=True)  # Field name made lowercase.
    posy = models.IntegerField(db_column='PosY', blank=True, null=True)  # Field name made lowercase.
    reserved = models.CharField(db_column='Reserved', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'td_videoshow'


class TwDatahistory(models.Model):
    dataid = models.CharField(db_column='DataId', max_length=40)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceId', max_length=40)  # Field name made lowercase.
    devicename = models.CharField(db_column='DeviceName', max_length=255)  # Field name made lowercase.
    collecttime = models.CharField(db_column='CollectTime', max_length=32)  # Field name made lowercase.
    devicestatus = models.IntegerField(db_column='DeviceStatus')  # Field name made lowercase.
    paramvalue = models.TextField(db_column='ParamValue')  # Field name made lowercase. This field type is a guess.
    alarminfo = models.TextField(db_column='AlarmInfo', blank=True,
                                 null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tw_datahistory'
        unique_together = (('DataId', 'DeviceId', 'CollectTime'),)


class TwDatarecent(models.Model):
    dataid = models.CharField(db_column='DataId', max_length=40)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceId', max_length=40)  # Field name made lowercase.
    devicename = models.CharField(db_column='DeviceName', max_length=255)  # Field name made lowercase.
    collecttime = models.CharField(db_column='CollectTime', max_length=32)  # Field name made lowercase.
    devicestatus = models.IntegerField(db_column='DeviceStatus')  # Field name made lowercase.
    paramvalue = models.TextField(db_column='ParamValue')  # Field name made lowercase. This field type is a guess.
    alarminfo = models.TextField(db_column='AlarmInfo', blank=True,
                                 null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tw_datarecent'
        unique_together = (('DataId', 'DeviceId', 'CollectTime'),)
