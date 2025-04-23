---
title: Python.NETを使用して複数のスレッドでセル値を同時に読み取る方法
linktitle: 複数のスレッド
type: docs
weight: 1800
url: /ja/python-net/reading-cell-values-in-multiple-threads-simultaneously/
description: Aspose.Cells for Python via .NET APIを使用して、複数のスレッドで同時にセル値を読む方法を学びます。
keywords: 複数のスレッドで同時にセル値を読む、Aspose.Cells Python マルチスレッド、複数スレッドでのデータ読み取り
---

{{% alert color="primary" %}}

複数のスレッドで同時にセル値を読み取る必要がある場合がよくあります。この記事ではその目的で Aspose.Cells の使用方法を説明します。

{{% /alert %}}

複数のスレッドで同時にセル値を読むには、[**worksheet.cells.multi_thread_reading**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/multi_thread_reading/)を**True**に設定します。設定しない場合、誤ったセル値を取得する可能性があります。

次のコード:

1. ワークブックを作成
1. シートを追加
1. 文字列値でシートを埋める
1. ランダムなセルから値を同時に読み取る2つのスレッドを作成
   読み取った値が正しい場合、何も起こりません。読み取った値が間違っている場合は、メッセージが表示されます。

この行をコメントアウトすると、次のメッセージが表示されます:

```python
test_workbook.worksheets[0].cells.multi_thread_reading = True
```

次のメッセージチェックがトリガーされます：

```python
if s != f"R{row}C{col}":
    print("This message will show when cells read values are incorrect")
```

それ以外の場合、セルから読み取ったすべての値が正しい場合、プログラムはメッセージを表示せずに実行されます。

```python
import threading
import random
import time
from aspose.cells import Workbook

test_workbook = None

def thread_loop():
    rand = random.Random()
    while True:
        try:
            row = rand.randint(0, 9999)
            col = rand.randint(0, 99)
            s = test_workbook.worksheets[0].cells.get(row, col).string_value
            if s != f"R{row}C{col}":
                print("This message will show up when cells read values are incorrect.")
        except:
            pass

def test_multi_threading_read():
    global test_workbook
    test_workbook = Workbook()
    test_workbook.worksheets.clear()
    test_workbook.worksheets.add("Sheet1")

    for row in range(10000):
        for col in range(100):
            test_workbook.worksheets[0].cells.get(row, col).value = f"R{row}C{col}"

    # Commenting this line will show a pop-up message
    # test_workbook.worksheets[0].cells.multi_thread_reading = True

    my_thread1 = threading.Thread(target=thread_loop, daemon=True)
    my_thread1.start()

    my_thread2 = threading.Thread(target=thread_loop, daemon=True)
    my_thread2.start()

    time.sleep(5)  # Sleep for 5 seconds

if __name__ == "__main__":
    test_multi_threading_read()
```

