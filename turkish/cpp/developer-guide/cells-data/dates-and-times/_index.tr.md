---
title: Tarih ve Saatleri C++ ile Nasıl Yönetilir
linktitle: Tarih ve Saatleri Nasıl Yönetilir
type: docs
weight: 600
url: /tr/cpp/how-to-manage-dates-and-times/
description: Aspose.Cells for C++ API kullanarak tarih ve saatleri nasıl yöneteceğinizi öğrenin.
keywords: Tarih ve Saatleri Nasıl Yönetilir, 1900 tarih sistemi, 1904 tarih sistemi, Tarih ve Saatleri Ayarlama, Tarih ve Saatleri Alma, Tarih ve Saatleri Yönetme, Tarih ve Saatleri Excel de Saklama, Tarih ve Saatleri Hücrelerde Gösterme.
---

## **Tarih ve Saatleri Excel'de Saklama**
Tarih ve saatler, hücrelerde sayı olarak saklanır. Bu nedenle, tarih ve saat içeren hücrelerin değerleri sayısal tiptedir. Bir tarih ve saati belirten sayı, tarih (tam sayı kısmı) ve saat (ondalık kısmı) bileşenlerinden oluşur. `Cell::GetDoubleValue()` yöntemi bu sayıyı döndürür.

## **Tarihleri ve Saatleri Aspose.Cells'de Gösterme**
Bir sayıyı tarih ve saat olarak göstermek için, hücreye gerekli tarih ve saat biçimini uygula, `Style::SetNumber()` veya `Style::SetCustom()` yöntemi ile. `Cell::GetDateTimeValue()` yöntemi, hücredeki sayının temsil ettiği tarih ve saati belirten `DateTime` nesnesini döndürür.
<br>
<image src="1.png" width="70%" />

## **Aspose.Cells'te iki tarih sistemi arasında nasıl geçiş yapılır**
MS-Excel, tarihleri seri değerler olarak adlandırılan sayılar olarak saklar. Bir seri değer, tarih sistemine göre ilk günden geçen günlerin sayısıdır. Excel, seri değerler için aşağıdaki tarih sistemlerini destekler:

1. 1900 tarih sistemi. İlk tarih 1 Ocak 1900'dür ve seri değeri 1'dir. Son tarih 31 Aralık 9999'dur ve seri değeri 2.958.465'tir. Bu tarih sistemi, ön tanımlı olarak çalışbook'ta kullanılır.
1. 1904 tarih sistemi. İlk tarih 1 Ocak 1904'tür ve onun seri değeri 0'dır. Son tarih 31 Aralık 9999'dur ve seri değeri 2.957.003'tür. Bu tarih sistemini çalışma kitabında kullanmak için, `Workbook::GetSettings()->SetDate1904(true)` özelliği ayarlayın.

Bu örnek, farklı tarih sistemlerinde aynı tarihte saklanan seri değerlerin farklı olduğunu göstermektedir.
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
Çıktı sonucu:
```
A1 is Numeric Value: 45253
use The 1904 date system====================
A2 is Numeric Value: 43791
```

## **Aspose.Cells'te DateTime Değerini Nasıl Ayarlar**
Bu örnek, A1 ve A2 hücrelerine `DateTime` değeri atar, A1'in özel biçimini ve A2'nin sayı biçimini ayarlar ve ardından değer türlerini çıktı olarak verir.

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

Çıktı sonucu:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
```

## **Aspose.Cells'te DateTime Değeri Nasıl Alınır**
Bu örnek, A1 ve A2 hücrelerine `DateTime` değeri atar, A1'in özel biçimini ve A2'nin sayı biçimini ayarlar, iki hücrenin değer türlerini kontrol eder ve ardından `DateTime` değeri ile biçimlendirilmiş string'i çıktı olarak verir.

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

Çıktı sonucu:
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
{{< app/cells/assistant language="cpp" >}}
