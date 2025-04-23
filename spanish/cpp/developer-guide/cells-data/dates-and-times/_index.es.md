---
title: Cómo gestionar fechas y horas con C++
linktitle: Cómo Gestionar Fechas y Horas
type: docs
weight: 600
url: /es/cpp/how-to-manage-dates-and-times/
description: Aprende cómo gestionar fechas y horas a través de la API Aspose.Cells for C++.
keywords: Cómo gestionar fechas y horas, sistema de fecha 1900, sistema de fecha 1904, establecer fechas y horas, obtener fechas y horas, gestionar fechas y horas, almacenar fechas y horas en Excel, mostrar fechas y horas en celdas.
---

## **Cómo almacenar fechas y horas en Excel**
Las fechas y horas se almacenan en las celdas como números. Por lo tanto, los valores de las celdas que contienen fechas y horas son del tipo numérico. Un número que especifica una fecha y hora consiste en componentes de fecha (parte entera) y hora (parte fraccionaria). El método `Cell::GetDoubleValue()` devuelve este número.

## **Cómo mostrar fechas y horas en Aspose.Cells**
Para mostrar un número como una fecha y hora, aplique el formato de fecha y hora requerido a la celda mediante el método `Style::SetNumber()` o `Style::SetCustom()`. El método `Cell::GetDateTimeValue()` devuelve el objeto `DateTime`, que especifica la fecha y hora que representa el número contenido en una celda.
<br>
<image src="1.png" width="70%" />

## **Cómo cambiar dos sistemas de fecha en Aspose.Cells**
MS-Excel almacena fechas como números que se llaman valores seriales. Un valor serial es un entero que representa el número de días transcurridos desde el primer día en el sistema de fecha. Excel admite los siguientes sistemas de fecha para los valores seriales:

1. El sistema de fecha 1900. La primera fecha es el 1 de enero de 1900 y su valor serial es 1. La última fecha es el 31 de diciembre de 9999 y su valor serial es 2,958,465. Este sistema de fecha se utiliza en el libro de trabajo de forma predeterminada.
1. El sistema de fechas 1904. La primera fecha es el 1 de enero de 1904, y su valor serial es 0. La última fecha es el 31 de diciembre de 9999, y su valor serial es 2,957,003. Para usar este sistema de fechas en el libro de trabajo, configure la propiedad `Workbook::GetSettings()->SetDate1904(true)`.

Este ejemplo muestra que los valores seriales almacenados en la misma fecha en diferentes sistemas de fecha son diferentes.
```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook workbook;
    workbook.GetSettings().SetDate1904(false);

    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell a1 = cells.Get(u"A1");
    a1.PutValue(45237.0);

    if (a1.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A1 is Numeric Value: " << a1.GetDoubleValue() << std::endl;
    }

    workbook.GetSettings().SetDate1904(true);
    std::cout << "use The 1904 date system====================" << std::endl;

    Cell a2 = cells.Get(u"A2");
    a2.PutValue(43775.0);

    if (a2.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A2 is Numeric Value: " << a2.GetDoubleValue() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
Resultado de la salida:
```
A1 is Numeric Value: 45253
use The 1904 date system====================
A2 is Numeric Value: 43791
```

## **Cómo establecer el valor de fecha y hora en Aspose.Cells**
Este ejemplo establece un valor `DateTime` en las celdas A1 y A2, configura el formato personalizado de A1 y el formato numérico de A2, y luego muestra los tipos de valor.

```c++
#include <iostream>
#include <ctime>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell a1 = cells.Get(u"A1");
    time_t now = time(nullptr);
    double oaDate1 = static_cast<double>(now) / (60 * 60 * 24) + 25569.0;
    a1.PutValue(oaDate1);

    if (a1.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A1 is Numeric Value: " << a1.IsNumericValue() << std::endl;
    }

    Style a1Style = a1.GetStyle();
    a1Style.SetCustom(u"mm-dd-yy hh:mm:ss", true);
    a1.SetStyle(a1Style);

    if (a1.GetType() == CellValueType::IsDateTime)
    {
        std::cout << "Cell A1 contains a DateTime value." << std::endl;
    }
    else
    {
        std::cout << "Cell A1 does not contain a DateTime value." << std::endl;
    }

    Cell a2 = cells.Get(u"A2");
    now = time(nullptr);
    double oaDate2 = static_cast<double>(now) / (60 * 60 * 24) + 25569.0;
    a2.SetValue(oaDate2);

    if (a2.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A2 is Numeric Value: " << a2.IsNumericValue() << std::endl;
    }

    Style a2Style = a2.GetStyle();
    a2Style.SetNumber(22);
    a2.SetStyle(a2Style);

    if (a2.GetType() == CellValueType::IsDateTime)
    {
        std::cout << "Cell A2 contains a DateTime value." << std::endl;
    }
    else
    {
        std::cout << "Cell A2 does not contain a DateTime value." << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

Resultado de la salida:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
```

## **Cómo obtener el valor de fecha y hora en Aspose.Cells**
Este ejemplo establece un valor `DateTime` en las celdas A1 y A2, configura el formato personalizado de A1 y el formato numérico de A2, verifica los tipos de valor de dos celdas y luego muestra el valor `DateTime` y la cadena formateada.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell a1 = cells.Get(u"A1");
    a1.PutValue(Date{2023, 5, 15});

    if (a1.GetType() == CellValueType::IsNumeric) {
        std::cout << "A1 is Numeric Value: " << a1.IsNumericValue() << std::endl;
    }

    Style a1Style = a1.GetStyle();
    a1Style.SetCustom(u"mm-dd-yy hh:mm:ss", true);
    a1.SetStyle(a1Style);

    if (a1.GetType() == CellValueType::IsDateTime) {
        std::cout << "Cell A1 contains a DateTime value." << std::endl;
        Date dateTimeValue = a1.GetDateTimeValue();
        std::cout << "A1 DateTime String Value: " << a1.GetStringValue().ToUtf8() << std::endl;
    }
    else {
        std::cout << "Cell A1 does not contain a DateTime value." << std::endl;
    }

    Cell a2 = cells.Get(u"A2");
    a2.PutValue(Date{2023, 5, 16});

    if (a2.GetType() == CellValueType::IsNumeric) {
        std::cout << "A2 is Numeric Value: " << a2.IsNumericValue() << std::endl;
    }

    Style a2Style = a2.GetStyle();
    a2Style.SetNumber(22);
    a2.SetStyle(a2Style);

    if (a2.GetType() == CellValueType::IsDateTime) {
        std::cout << "Cell A2 contains a DateTime value." << std::endl;
        Date dateTimeValue = a2.GetDateTimeValue();
        std::cout << "A2 DateTime String Value: " << a2.GetStringValue().ToUtf8() << std::endl;
    }
    else {
        std::cout << "Cell A2 does not contain a DateTime value." << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

Resultado de la salida:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A1 DateTime Value: 11/23/2023 5:59:09 PM
A1 DateTime String Value: 11-23-23 17:59:09
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
A2 DateTime Value: 11/23/2023 5:59:09 PM
A2 DateTime String Value: 11/23/2023 17:59
```
