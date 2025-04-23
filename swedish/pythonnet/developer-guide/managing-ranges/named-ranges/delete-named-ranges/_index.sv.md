---
title: Ta bort namngivna områden
type: docs
weight: 90
url: /sv/python-net/delete-named-ranges/
description: Du kan lära dig hur du tar bort definierade namn eller namngivna områden från Excel eller OpenOffice filer med Aspose.Cells för Python via .Net.
keywords: Python Excel bibliotek, Python Ta bort dubbla definierade namn, Python Ta bort dubbletter av definerade namn.
---

## **Introduktion**
Om det finns för många definierade namn eller namngivna områden i Excel-filerna måste vi rensa några så att de inte längre refereras till.

## **Ta bort namngivet område i MS Excel**

För att ta bort ett namngivet område från Excel kan du följa dessa steg:
1. Öppna Microsoft Excel och öppna arbetsboken som innehåller det namngivna området.
2. Gå till fliken "Formler" i Excel-ribbonen.
3. Klicka på knappen "Namnhanterare" i gruppen "Definierade namn". Detta öppnar dialogrutan för Namnhanterare.
4. I dialogrutan för Namnhanterare väljer du det namngivna området du vill ta bort.
5. Klicka på knappen "Ta bort". Bekräfta borttagningen vid behov.
6. Klicka på knappen "Stäng" för att stänga dialogrutan för Namnhanterare.
7. Spara arbetsboken för att behålla ändringarna.

## **Tar bort namngivet område med Aspose.Cells for .Net**
Med Aspose.Cells för .Net kan du ta bort namnintervall eller definierade namn genom [text](https://reference.aspose.com/cells/python-net/aspose.cells.namecollection/remove_a_name/#str) i listan.

```python
from aspose.cells import Workbook
import aspose.cells
import os
import pytest
# The path to the documents directory
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Instantiate a new Workbook
workbook = Workbook(os.path.join(data_dir, "Book1.xlsx"))

# Get all the worksheets in the book
worksheets = workbook.worksheets

# Delete a named range by text
worksheets.names.remove_a_name("NamedRange")


# Save the workbook to retain the changes
workbook.save(os.path.join(data_dir, "Book2.xlsx"))
```

Observera: Om det definierade namnet används av formler kan det inte tas bort. Vi kan bara ta bort formeln för det definierade namnet.

## **Tar bort vissa namngivna områden**
När vi tar bort ett definierat namn måste vi kontrollera om det används av alla formler i filen.
För att förbättra prestandan för att ta bort namngivna områden kan vi ta bort vissa tillsammans.

```python
from aspose.cells import Workbook
import aspose.cells
import os
import pytest
# Instantiate a new Workbook
workbook = Workbook("testcase/data/Book1.xlsx")

# Get all the worksheets in the book
worksheets = workbook.worksheets

# Delete some defined names
worksheets.names.remove_names_by_array(["NamedRange1", "NamedRange2"])

# Save the workbook to retain the changes
workbook.save("Book2.xlsx")
```


## **Ta bort dubbla definierade namn**
Vissa Excel-filer korrumperas eftersom vissa definierade namn är dubletter. Så vi kan ta bort dessa dubbla namn för att reparera filen.

```python
from aspose.cells import Workbook
import aspose.cells
import os
import pytest
# Instantiate a new Workbook
workbook = Workbook("testcase/data/Book1.xlsx")

# Get all the worksheets in the book
worksheets = workbook.worksheets

# Delete duplicate defined names
worksheets.names.remove_duplicate_names()

# Save the workbook to retain the changes
workbook.save("Book2.xlsx")
```
