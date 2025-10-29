---
title: Lecture des valeurs des cellules en plusieurs threads simultanément avec Python.NET
linktitle: Plusieurs threads
type: docs
weight: 1800
url: /fr/python-net/reading-cell-values-in-multiple-threads-simultaneously/
description: Découvrez comment lire les valeurs des cellules en plusieurs threads simultanément en utilisant Aspose.Cells pour Python via .NET API.
keywords: Lecture des valeurs des cellules en plusieurs threads simultanément, Aspose.Cells Python Multi threads, lecture de données en plusieurs threads
---

{{% alert color="primary" %}}

La nécessité de lire les valeurs de cellule dans plusieurs threads simultanément est une exigence courante. Cet article explique comment utiliser Aspose.Cells à cette fin.

{{% /alert %}}

Pour lire les valeurs des cellules dans plus d'un thread simultanément, définissez [**worksheet.cells.multi_thread_reading**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/multi_thread_reading/) à **True**. Si vous ne le faites pas, vous pourriez obtenir des valeurs incorrectes.

Le code suivant :

1. Crée un classeur
1. Ajoute une feuille de calcul
1. Remplit la feuille avec des valeurs de chaîne
1. Crée deux threads qui lisent simultanément des valeurs à partir de cellules aléatoires
   Si les valeurs lues sont correctes, rien ne se passe. Si les valeurs lues sont incorrectes, un message est affiché.

Si vous commentez cette ligne :

```python
test_workbook.worksheets[0].cells.multi_thread_reading = True
```

alors le message suivant sera déclenché :

```python
if s != f"R{row}C{col}":
    print("This message will show when cells read values are incorrect")
```

Sinon, le programme s'exécute sans afficher de message, ce qui signifie que toutes les valeurs lues dans les cellules sont correctes.

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

{{< app/cells/assistant language="python-net" >}}
