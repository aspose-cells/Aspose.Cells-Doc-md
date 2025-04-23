---
title: C++ ile Ad ile Metin Kutusuna Erişim
linktitle: Ada Göre Metin Kutusuna Eriş
type: docs
weight: 230
url: /tr/cpp/access-the-text-box-by-the-name/
description: Aspose.Cells for C++ kullanarak ad ile metin kutusuna nasıl erişileceğini öğrenin.
---

## Ada Göre Metin Kutusuna Eriş

 Eskiden, metin kutularına [**Worksheet.GetTextBoxes()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettextboxes/) koleksiyonundan indeks kullanılarak erişilirdi, ama şimdi koleksiyondan isimle de erişebilirsiniz. Bu, zaten adını bildiğiniz takdirde metin kutusuna hızlı ve kullanışlı bir erişim sağlar.

 Aşağıdaki örnek kod ilk olarak bir metin kutusu oluşturur, ona metin ve ad atar. Sonra, ad ile aynı metin kutusuna erişir ve içeriğini yazdırır.

### C++ ile isimle metin kutusuna erişim kodu

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Create an object of the Workbook class
    Workbook workbook;

    // Access first worksheet from the collection
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add the TextBox to the worksheet
    int idx = sheet.GetTextBoxes().Add(10, 10, 10, 10);

    // Access newly created TextBox using its index & name it
    TextBox tb1 = sheet.GetTextBoxes().Get(idx);
    tb1.SetName(u"MyTextBox");

    // Set text for the TextBox
    tb1.SetText(u"This is MyTextBox");

    // Access the same TextBox via its name
    TextBox tb2 = sheet.GetTextBoxes().Get(u"MyTextBox");

    // Display the text of the TextBox accessed via name
    std::cout << tb2.GetText().ToUtf8() << std::endl;

    std::cout << "Press any key to continue..." << std::endl;
    std::cin.get();

    Aspose::Cells::Cleanup();
}
```

### Örnek kod tarafından oluşturulan konsol çıktısı

Yukarıdaki örnek kodun konsol çıktısı burada gösterilmektedir.

{{< highlight java >}}

This is MyTextBox

{{< /highlight >}}
