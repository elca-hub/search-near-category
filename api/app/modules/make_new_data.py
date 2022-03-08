import csv, random, string

def make_new_data (csv_file, num):
  def randomname(n): # ランダムな文字列を生成
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))
  def make_body_data (num): # ランダムな数値を持たせたリストを生成
    bodydata = []
    min_ran = 0
    max_ran = 100
    for i in range(num):
      append_data = []
      append_data.append(i) # id
      append_data.append(randomname(10)) # name
      fun = random.randint(min_ran, max_ran)
      sad = random.randint(min_ran, max_ran - fun)
      imp = random.randint(fun, max_ran)
      ang = random.randint(min_ran, max_ran - imp)
      append_data.append(fun) # fun
      append_data.append(sad) # sad
      append_data.append(imp) # imp
      append_data.append(ang) # ang
      bodydata.append(append_data)
    return bodydata
  header = ['id', 'name', 'fun', 'sad', 'imp', 'ang']
  body = make_body_data(num)

  with open('./modules/csv/' + csv_file, 'w') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(header)
    writer.writerows(body)
