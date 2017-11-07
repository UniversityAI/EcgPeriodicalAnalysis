class DataReaderMITBIH:
  def __init__(self, filename, sampleRate):
    self.filename = filename
    self.sampleRate = sampleRate

  def readRriListFromFile(self):
    with open(self.filename, 'r') as f:
      r_peak_pos_list = f.read().split(",")
    r_peak_pos_list = [x for x in r_peak_pos_list if len(x.strip()) > 0]
    r_peak_pos_list = map(int, r_peak_pos_list)

    r_peak_pos_in_ms_list = []
    for pos in r_peak_pos_list:
      r_peak_pos_in_ms_list.append(pos*1000.0/self.sampleRate)

    rri_list = []
    for idx in range(0, len(r_peak_pos_in_ms_list)-1):
      rri_list.append(r_peak_pos_in_ms_list[idx+1] - r_peak_pos_in_ms_list[idx])

    return rri_list

  def prepareDataSet(self, time_steps_for_rnn, readFromFile=False):
    dataSet = []
    rriList = self.readRriListFromFile()

    idx = 0
    while (idx+time_steps_for_rnn) < len(rriList):
      dataList = [x for x in rriList[idx:idx+time_steps_for_rnn]]
      label = rriList[idx+time_steps_for_rnn]
      dataSet.append({'data':dataList, 'label': label})
      idx=idx+1

    return dataSet

