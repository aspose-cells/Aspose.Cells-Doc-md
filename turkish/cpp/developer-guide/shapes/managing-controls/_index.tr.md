---
title: C++ ile Kontrolleri Yönetme
linktitle: Kontrolleri Yönetme
type: docs
weight: 150
url: /tr/cpp/managing-controls/
description: Aspose.Cells kullanarak C++ ile çalışma sayfalarında çeşitli kontroller (çizgiler, dikdörtgenler, yaylar, oval, dönen kutular, kaydırıcılar ve grup kutuları gibi) nasıl eklenir ve yönetilir öğrenin.
---

## **Giriş**

Geliştiriciler, metin kutuları, onay kutuları, radyo düğmeleri, kombinasyon kutuları, etiketler, düğmeler, çizgiler, dikdörtgenler, yaylar, oval, dönen kutular, kaydırıcılar, grup kutuları ve diğer çizim nesneleri gibi farklı nesneleri ekleyebilir. Aspose.Cells, tüm çizim nesnelerini içeren `Aspose::Cells::Drawing` isim alanını sağlar. Ancak, henüz desteklenmeyen birkaç çizim nesnesi veya şekil mevcuttur. Bu çizim nesnelerini Microsoft Excel kullanarak tasarımcı çalışma kitabında oluşturup ardından Aspose.Cells ile içe aktarabilirsiniz. Aspose.Cells, tasarımcı çalışma kitabından bu şekil nesnelerini yüklemenize ve bunları oluşturulan dosyaya yazmanıza olanak tanır.

## **Bir Çalışma Sayfasına Metin Kutusu Denetimi Ekleme**

Raporda önemli bilgileri vurgulamanın bir yolu metin kutusu kullanmaktır. Örneğin, şirket adını vurgulamak veya en yüksek satışı olan coğrafi bölgeyi belirtmek için metin ekleyebilirsiniz. Aspose.Cells, yeni bir metin kutusu eklemek için kullanılan [**TextBoxCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textboxcollection/) sınıfını sağlar. Tüm türde ayarları tanımlamak için kullanılan başka bir sınıf olan [**TextBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textbox/) vardır. Önemli üyeleri vardır:

- [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) özelliği yerleştirme türünü belirtir.
- [**Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) özelliği yazı tipi özelliklerini belirtir.
- [**AddHyperlink**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/addhyperlink/) methodu, metin kutusu için bir bağlantıyı ekler.
- [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) özelliği, metin kutusunun dolgu biçimini ayarlamak için kullanılan bir [**MsoFillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/msofillformat/) nesnesini döndürür.
- [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) özelliği, metin kutusu çizgisi için stil ve kalınlık genellikle kullanılan bir [**MsoLineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/msolineformat/) nesnesi döndürür.
- [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) özelliği giriş metnini belirtir.

Aşağıdaki örnek, çalışma kitabının ilk çalışma sayfasında iki metin kutusu oluşturur. İlk metin kutusu farklı biçim ayarlarıyla donatılmıştır. İkincisi ise basit bir tanedir.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // The path to the documents directory.
    U16String dataDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate a new Workbook.
    Workbook workbook;

    // Get the first worksheet in the book.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a new textbox to the collection.
    int32_t textboxIndex = worksheet.GetTextBoxes().Add(2, 1, 160, 200);

    // Get the textbox object.
    TextBox textbox0 = worksheet.GetTextBoxes().Get(textboxIndex);

    // Fill the text.
    textbox0.SetText(u"ASPOSE______The .NET & JAVA Component Publisher!");

    // Set the placement.
    textbox0.SetPlacement(PlacementType::FreeFloating);

    // Set the font color.
    textbox0.GetFont().SetColor(Color::Blue());

    // Set the font to bold.
    textbox0.GetFont().SetIsBold(true);

    // Set the font size.
    textbox0.GetFont().SetSize(14);

    // Set font attribute to italic.
    textbox0.GetFont().SetIsItalic(true);

    // Add a hyperlink to the textbox.
    textbox0.AddHyperlink(u"http://www.aspose.com/");

    // Get the fill format of the textbox.
    FillFormat fillFormat = textbox0.GetFill();

    // Get the line format type of the textbox.
    LineFormat lineFormat = textbox0.GetLine();

    // Set the line weight.
    lineFormat.SetWeight(6.0);

    // Set the dash style to squaredot.
    lineFormat.SetDashStyle(MsoLineDashStyle::SquareDot);

    // Add another textbox.
    textboxIndex = worksheet.GetTextBoxes().Add(15, 4, 85, 120);

    // Get the second textbox.
    TextBox textbox1 = worksheet.GetTextBoxes().Get(textboxIndex);

    // Input some text to it.
    textbox1.SetText(u"This is another simple text box");

    // Set the placement type as the textbox will move and resize with cells.
    textbox1.SetPlacement(PlacementType::MoveAndSize);

    // Save the excel file.
    workbook.Save(dataDir + u"book1.out.xls");

    Aspose::Cells::Cleanup();
}
```

## **Tasarımcı Elektronik Tablolarda Metin Kutusu Denetimlerini Manipüle Etme**

Aspose.Cells, ayrıca tasarımcı elektronik tablolardaki metin kutularına erişmenizi ve bunları manipüle etmenizi sağlar. Levhada metin kutuları koleksiyonunu almak için [**Worksheet.GetTextBoxes()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettextboxes/) özelliğini kullanın.

Aşağıdaki örnek yukarıdaki örnekte oluşturduğumuz Microsoft Excel dosyasını kullanır. İki metin kutusunun metin dizelerini alır ve ikinci metin kutusunun metnini değiştirerek dosyayı kaydeder.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // The path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the existing excel file.
    Workbook workbook(srcDir + u"book1.xls");

    // Get the first worksheet in the workbook.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the first textbox object.
    TextBox textbox0 = worksheet.GetTextBoxes().Get(0);

    // Obtain the text in the first textbox.
    U16String text0 = textbox0.GetText();

    // Get the second textbox object.
    TextBox textbox1 = worksheet.GetTextBoxes().Get(1);

    // Obtain the text in the second textbox.
    U16String text1 = textbox1.GetText();

    // Change the text of the second textbox.
    textbox1.SetText(u"This is an alternative text");

    // Save the excel file.
    workbook.Save(srcDir + u"output.out.xls");

    Aspose::Cells::Cleanup();
}
```

## **Bir Çalışma Sayfasına Onay Kutusu Denetimi Ekleme**

Onay kutuları, bir kullanıcının doğru veya yanlış gibi iki seçenek arasında seçim yapmasına olanak tanımak istiyorsanız kullanışlıdır. Örneğin, belirli bir edinimi hesaba katıp katmayacağını belirtmek istediğiniz bir finansal projeksiyon çalışma sayfası geliştirdiniz. Bu durumda, çalışma sayfasının üst kısmına bir onay kutusu yerleştirmek isteyebilirsiniz. Daha sonra bu onay kutusunun durumunu başka bir hücreye bağlayabilirsiniz; böylece onay kutusu seçiliyken, hücrenin değeri True olur; seçilmediğinde, hücrenin değeri False olur.

### **Microsoft Excel Kullanımı**

Çalışma sayfanıza bir onay kutusu denetimi yerleştirmek için şu adımları izleyin:

1. Formlar araç çubuğunun görüntülendiğinden emin olun.
1. Formlar araç çubuğunda **Onay Kutusu** aracını tıklayın.
1. Çalışma sayfanızda, onay kutusunu ve onay kutusunun yanındaki etiketi içerecek dikdörtgeni tanımlamak için tıklayın ve sürükleyin.
1. Onay kutusu yerleştirildikten sonra fare imleci etiket alanına kaydırın ve etiketi değiştirin.
1. **Hücre Bağlantısı** alanında, bu onay kutusunun bağlanması gereken hücrenin adresini belirtin.
1. **Tamam**'ı tıklayın.

### **Aspose.Cells Kullanımı**

Aspose.Cells, yeni bir onay kutusu eklemek için kullanılan [**CheckBoxCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/checkboxcollection/) sınıfını sağlar. İşte onay kutusunu temsil eden başka bir sınıf olan [**Aspose::Cells::Drawing::CheckBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/checkbox/). Önemli bazı üyelere sahiptir:

- [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) özelliği, onay kutusuna bağlı olan bir hücreyi belirtir.
- [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) özelliği, onay kutusu ile ilişkilendirilmiş metin dizisini belirtir. Bu, onay kutusunun etiketidir.
- [**GetValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/checkbox/getvalue/) özelliği, onay kutusunun işaretli olup olmadığını belirtir.

Aşağıdaki örnek, bir çalışma sayfasına onay kutusu eklemenin nasıl yapıldığını göstermektedir.

```c++
#include <iostream>
#include <Aspose.Cells.h>
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Creating a new Workbook instance
    Workbook excelbook = Workbook();

    // Get the first worksheet
    Worksheet worksheet = excelbook.GetWorksheets().Get(0);

    // Add a checkbox to the first worksheet in the workbook
    int32_t index = worksheet.GetCheckBoxes().Add(5, 5, 100, 120);

    // Get the checkbox object
    Drawing::CheckBox checkbox = worksheet.GetCheckBoxes().Get(index);

    // Set its text string
    checkbox.SetText(u"Click it!");

    // Get cells collection and set B1 cell value
    Cells cells = worksheet.GetCells();
    Cell cellB1 = cells.Get(u"B1");
    cellB1.PutValue(u"LnkCell");

    // Set B1 cell as a linked cell for the checkbox
    checkbox.SetLinkedCell(u"B1");

    // Check the checkbox by default
    checkbox.SetValue(true);

    // Save the excel file
    excelbook.Save(u"book1.out.xls");

    Aspose::Cells::Cleanup();
}
```

## **Çalışma Sayfasına Radyo Düğmesi Denetimi Ekleme**

Radyo düğmesi veya seçenek düğmesi, yuvarlak bir kutudan oluşan bir denetimdir. Kullanıcı, yuvarlak kutuyu seçerek kararını verir. Radyo düğmesi genellikle, diğerleri ile birlikte olacak şekilde, eğer her zaman değilse eşlik eder. Bu tür radyo düğmeleri grup olarak görünür ve davranır. Kullanıcı, sadece birini seçerek hangi düğmenin geçerli olduğuna karar verir. Kullanıcı bir düğmeye tıkladığında doldurulur. Grubun içindeki bir düğme seçildiğinde, aynı gruba ait düğmeler boş olur.

### **Microsoft Excel Kullanımı**

Çalışma sayfanıza bir Radyo Düğmesi denetimi yerleştirmek için şu adımları izleyin:

1. **Formlar** araç çubuğunun görüntülendiğinden emin olun.
1. **Seçenek Düğmesi** aracına tıklayın.
1. Çalışma sayfasında, seçenek düğmesini ve yanındaki etiketi tutacak dikdörtgeni tanımlamak için tıklayın ve sürükleyin.
1. Radyo düğmesi çalışma sayfasına yerleştirildikten sonra, fare imleci etiket bölgesine hareket ettirin ve etiketi değiştirin.
1. **Hücre Bağlantısı** alanında, bu radyo düğmesinin bağlanması gereken hücrenin adresini belirtin.
1. **Tamam**'a tıklayın.

### **Aspose.Cells Kullanımı**

[**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) sınıfı, bir çalışma sayfasına radyo düğmesi eklemek için kullanılan [**AddRadioButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addradiobutton/) adlı bir yönteme sahiptir. Bu yöntem, bir [**Aspose::Cells::Drawing::RadioButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/radiobutton/) nesnesi döndürür. [**Aspose::Cells::Drawing::RadioButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/radiobutton/) sınıfı, bir seçenek düğmesini temsil eder. Bazı önemli üyeleri vardır:

- [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) özelliği, radyo düğmesine bağlı olan bir hücreyi belirtir.
- [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) özelliği, radyo düğmesi ile ilişkilendirilmiş metin dizisini belirtir. Bu, radyo düğmesinin etiketidir.
- [**IsChecked**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/radiobutton/ischecked/) özelliği, radyo düğmesinin işaretli olup olmadığını belirtir.
- [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) özelliği, seçenek düğmesinin doldurma biçimini belirtir.
- [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) özelliği, seçenek düğmesinin çizgi biçimi stillerini belirtir.

Aşağıdaki örnek, bir çalışma sayfasına radyo düğmeleri eklemenin nasıl yapıldığını göstermektedir. Örnek, yaş gruplarını temsil eden üç radyo düğmesi ekler.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate a new Workbook.
    Workbook excelbook;

    // Get the first worksheet
    Worksheet sheet = excelbook.GetWorksheets().Get(0);

    // Get cells collection
    Cells cells = sheet.GetCells();

    // Insert a value in C2
    Cell cellC2 = cells.Get(u"C2");
    cellC2.PutValue(u"Age Groups");

    // Set the font text bold.
    Style style = cellC2.GetStyle();
    Font font = style.GetFont();
    font.SetIsBold(true);

    // Apply the style back
    cellC2.SetStyle(style);

    // Add radio buttons to the first sheet.
    ShapeCollection shapes = sheet.GetShapes();

    // Create first radio button
    RadioButton radio1= shapes.AddRadioButton(3, 0, 2, 0, 30, 110);


    // Set its text string.
    radio1.SetText(u"20-29");
    // Set A1 cell as a linked cell for the radio button.
    radio1.SetLinkedCell(u"A1");
    // Make the radio button 3-D.
    radio1.SetShadow(true);
    // Set the weight of the radio button.
    LineFormat line1 = radio1.GetLine();
    line1.SetWeight(4);
    // Set the dash style of the radio button.
    line1.SetDashStyle(MsoLineDashStyle::Solid);

    // Create second radio button
    RadioButton radio2 = shapes.AddRadioButton(6, 0, 2, 0, 30, 110);
    // Set its text string.
    radio2.SetText(u"30-39");
    // Set A1 cell as a linked cell for the radio button.
    radio2.SetLinkedCell(u"A1");
    // Make the radio button 3-D.
    radio2.SetShadow(true);
    // Set the weight of the radio button.
    LineFormat line2 = radio2.GetLine();
    line2.SetWeight(4);
    // Set the dash style of the radio button.
    line2.SetDashStyle(MsoLineDashStyle::Solid);

    // Create third radio button
    RadioButton radio3=shapes.AddRadioButton(9, 0, 2, 0, 30, 110);

    // Set its text string.
    radio3.SetText(u"40-49");
    // Set A1 cell as a linked cell for the radio button.
    radio3.SetLinkedCell(u"A1");
    // Make the radio button 3-D.
    radio3.SetShadow(true);
    // Set the weight of the radio button.
    LineFormat line3 = radio3.GetLine();
    line3.SetWeight(4);
    // Set the dash style of the radio button.
    line3.SetDashStyle(MsoLineDashStyle::Solid);

    // Save the excel file.
    excelbook.Save(srcDir + u"book1.out.xls");

    Aspose::Cells::Cleanup();
}
```

## **Çalışma Sayfasına Kombinasyon Kutusu Denetimi Ekleme**

Veri girişini kolaylaştırmak veya tanımladığınız belirli öğelerle girişleri sınırlamak için, işte çalışma sayfanızda başka yerlerdeki hücrelerden derlenen geçerli girişlerin bir combo kutusu veya açılır liste oluşturabilirsiniz. Bir hücre için bir açılır liste oluşturduğunuzda, o hücrenin yanında bir ok gösterilir. O hücredeki bilgiyi girmek için ok'a tıklayın ve ardından istediğiniz girişi tıklayın.

### **Microsoft Excel Kullanımı**

Çalışma sayfanıza bir kombinasyon kutusu denetimi yerleştirmek için şu adımları izleyin:

1. **Formlar** araç çubuğunun görüntülendiğinden emin olun.
1. **Kombo Kutusu** aracını tıklayın.
1. Çalışma sayfanızda, kombo kutusunu içerecek dikdörtgeni tanımlamak için tıklayıp sürükleyin.
1. Kombo kutusu çalışma sayfasına yerleştirildikten sonra, denetimi sağ tıklayarak **Format Kontrolü** tıklayın ve girdi aralığını belirtin.
1. **Hücre Bağlantısı** alanında, bu kombo kutusunun bağlanacağı hücrenin adresini belirtin.
1. **Tamam**'ı tıklayın.

### **Aspose.Cells Kullanımı**

[**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) sınıfı, çalışma sayfasına kombo kutu denetimi eklemek için kullanılan [**AddComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addcombobox/) adında bir yöntem sağlar. Yöntem bir [**Aspose::Cells::Drawing::ComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/) nesnesi döndürür. [**Aspose::Cells::Drawing::ComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/) sınıfı bir kombo kutusunu temsil eder. Önemli bazı üyeleri vardır:

- [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) özelliği kombo kutusuna bağlı olan bir hücreyi belirtir.
- [**GetInputRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getinputrange/) özelliği, kombo kutusunu doldurmak için kullanılan çalışma sayfası aralığını belirtir.
- [**GetDropDownLines()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/getdropdownlines/) özelliği, bir kombo kutusunun açılır kısmında görüntülenen liste satırlarının sayısını belirtir.
- [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/getshadow/) özelliği, kombo kutusunun 3B gölgelendirmeye sahip olup olmadığını belirtir.

Aşağıdaki örnek, çalışma sayfasına bir kombo kutusu eklemenin nasıl yapıldığını göstermektedir.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a new Workbook.
    Workbook workbook;

    // Get the first worksheet.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get the worksheet cells collection.
    Cells cells = sheet.GetCells();

    // Input a value.
    Cell cellB3 = cells.Get(u"B3");
    cellB3.PutValue(u"Employee:");

    // Set it bold.
    Style style = cellB3.GetStyle();
    style.SetIsBorderApplied(true);
    cellB3.SetStyle(style);

    // Input some values that denote the input range for the combo box.
    cells.Get(u"A2").PutValue(u"Emp001");
    cells.Get(u"A3").PutValue(u"Emp002");
    cells.Get(u"A4").PutValue(u"Emp003");
    cells.Get(u"A5").PutValue(u"Emp004");
    cells.Get(u"A6").PutValue(u"Emp005");
    cells.Get(u"A7").PutValue(u"Emp006");

    // Add a new combo box.
    ComboBox comboBox = sheet.GetShapes().AddComboBox(2, 0, 2, 0, 22, 100);

    // Cleanup Aspose resources
    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Etiket Denetimi Ekleme**

Etiketler, kullanıcılara bir elektronik tablonun içeriği hakkında bilgi vermenin bir yolu olarak kullanılır. Aspose.Cells, çalışma sayfasına etiket eklemeyi ve bunları manipüle etmeyi mümkün kılar. [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) sınıfı, çalışma sayfasına etiket denetimi eklemek için kullanılan [**AddLabel**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlabel/) adında bir yöntem sağlar. Yöntem bir [**Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/) nesnesi döndürür. [**Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/) sınıfı, çalışma sayfasında bir etiketi temsil eder. Önemli bazı üyeleri vardır:

- [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) yöntemi, bir etiketin açıklama dizgisini belirtir.
- [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) yöntemi, etiketin çalışma sayfasındaki hücrelere bağlanma şeklini belirtir.

Aşağıdaki örnek, çalışma sayfasına bir etiket eklemenin nasıl yapıldığını göstermektedir.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new Workbook
    Workbook workbook;

    // Get the first worksheet in the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add a new label to the worksheet
    Label label = sheet.GetShapes().AddLabel(2, 0, 2, 0, 60, 120);

    // Set the caption of the label
    label.SetText(u"This is a Label");

    // Set the Placement Type, the way the Label is attached to the cells
    label.SetPlacement(PlacementType::FreeFloating);

    // Save the file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Label added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Liste Kutusu Denetimi Ekleme**

Bir liste kutusu denetimi, tek ya da çoklu öğe seçimine izin veren bir liste denetimi oluşturur.

### **Microsoft Excel Kullanımı**

Bir liste kutusu denetimini çalışma sayfasına yerleştirmek için:

1. **Formlar** araç çubuğunun görüntülendiğinden emin olun.
1. **Liste Kutusu** aracını tıklayın.
1. Çalışma sayfanızda, liste kutusunu içerecek dikdörtgeni tanımlamak için tıklayıp sürükleyin.
1. Liste kutusu çalışma sayfasına yerleştirildikten sonra, denetimi sağ tıklayarak **Format Kontrolü** tıklayın ve girdi aralığını belirtin.
1. **Hücre Bağlantısı** alanında, bu liste kutusunun bağlanacağı hücrenin adresini belirtin ve seçim tipi (Tekli, Çoklu, Genişlet) özniteliğini belirtin.
1. **Tamam**'a tıklayın.

### **Aspose.Cells Kullanımı**

[**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) sınıfı, çalışma sayfasına liste kutusu denetimi eklemek için kullanılan [**AddListBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlistbox/) adında bir yöntem sağlar. Yöntem bir [**Aspose::Cells::Drawing::ListBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/listbox/) nesnesi döndürür. [**ListBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/listbox/) sınıfı bir liste kutusunu temsil eder. Önemli bazı üyeleri vardır:

- [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) method, bir liste kutusuna bağlı olan hücreyi belirtir.
- [**GetInputRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getinputrange/) method, liste kutusunu doldurmak için kullanılan çalışma sayfası hücre aralığını belirtir.
- [**SelectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/selectiontype/) method, liste kutusunun seçim kipini belirtir.
- [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/listbox/getshadow/) methodı, liste kutusunun 3D gölgelemeye sahip olup olmadığını gösterir.

Aşağıdaki örnek, çalışma sayfasına liste kutusu nasıl eklenir gösterir.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new Workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get the worksheet cells collection
    Cells cells = sheet.GetCells();

    // Input a value
    cells.Get(U16String(u"B3")).PutValue(U16String(u"Choose Dept:"));

    // Set it bold
    Style style = cells.Get(U16String(u"B3")).GetStyle();
    Font font = style.GetFont();
    font.SetIsBold(true);
    cells.Get(U16String(u"B3")).SetStyle(style);

    // Input some values that denote the input range for the list box
    cells.Get(U16String(u"A2")).PutValue(U16String(u"Sales"));
    cells.Get(U16String(u"A3")).PutValue(U16String(u"Finance"));
    cells.Get(U16String(u"A4")).PutValue(U16String(u"MIS"));
    cells.Get(U16String(u"A5")).PutValue(U16String(u"R&D"));
    cells.Get(U16String(u"A6")).PutValue(U16String(u"Marketing"));
    cells.Get(U16String(u"A7")).PutValue(U16String(u"HRA"));

    // Add a new list box
    ListBox listBox = sheet.GetShapes().AddListBox(2, 0, 3, 0, 122, 100);

    // Set the placement type
    listBox.SetPlacement(PlacementType::FreeFloating);

    // Set the linked cell
    listBox.SetLinkedCell(U16String(u"A1"));

    // Set the input range
    listBox.SetInputRange(U16String(u"A2:A7"));

    // Set the selection type
    listBox.SetSelectionType(SelectionType::Single);

    // Set the list box with 3-D shading
    listBox.SetShadow(true);

    // Save the file
    workbook.Save(outDir + u"book1.out.xls");

    Aspose::Cells::Cleanup();
}
```

## **Bir Çalışma Sayfasına Düğme Kontrolü Ekleme**

Düğmeler bazı işlemleri gerçekleştirmek için kullanışlıdır. Bazen düğmeye VBA Makrosu atamak veya bir web sayfasını açmak için bir bağlantı atamak faydalı olabilir.

### **Microsoft Excel Kullanımı**

Bir düğme kontrolünü çalışma sayfanıza yerleştirmek için:

1. **Formlar** araç çubuğunun görüntülendiğinden emin olun.
1. **Düğme** aracını tıklayın.
1. Çalışma sayfanızdaki alanda, düğmeyi tutacak dikdörtgeni tanımlamak için tıklayın ve sürükleyin.
1. Liste kutusu çalışma sayfasına yerleştirildikten sonra, denetim üzerinde sağ tıklayın ve sonra **Denetim Biçimi'ni** seçin, ardından VBA Makrosunu ve ilgili yazı tipi, hizalama, boyut, kenar boşluğu vb. özellikleri belirtin.
1. **Tamam**'ı tıklayın.

### **Aspose.Cells Kullanımı**

[**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) sınıfı, çalışma sayfasına bir düğme kontrolü eklemek için kullanılan [**AddButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addbutton/) adında bir yöntem sağlar. Yöntem bir [**Aspose::Cells::Drawing::Button**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/button/) nesnesi döndürür. [**Aspose::Cells::Drawing::Button**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/button/) sınıfı bir düğmeyi temsil eder. Bazı önemli üyelere sahiptir:

- [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) özelliği, düğmenin başlığını belirtir.
- [**Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) özelliği, düğme denetiminin etiketi için yazı tipi özniteliklerini belirtir.
- [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) özelliği, [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/), düğmenin çalışma sayfasındaki hücrelere nasıl bağlandığını belirtir.
- [**AddHyperlink**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/addhyperlink/) özelliği, düğme denetimi için bir bağlantı ekler. Düğmeye tıklamak ilgili URL'ye gid will navigate to related URL.

Aşağıdaki örnek, çalışma sayfasına bir düğme eklemenin nasıl yapılacağını gösterir.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a new Workbook
    Workbook workbook;

    // Get the first worksheet in the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add a new button to the worksheet
    Drawing::Button button = sheet.GetShapes().AddButton(2, 0, 2, 0, 28, 80);

    // Set the caption of the button
    button.SetText(u"Aspose");

    // Set the Placement Type, the way the Button is attached to the cells
    button.SetPlacement(PlacementType::FreeFloating);

    // Set the font name
    Font font = button.GetFont();
    font.SetName(u"Tahoma");

    // Set the caption string bold
    font.SetIsBold(true);

    // Set the color to blue
    font.SetColor(Color::Blue());

    // Set the hyperlink for the button
    button.AddHyperlink(u"http://www.aspose.com/");

    // Save the file
    workbook.Save(srcDir + u"book1.out.xls");

    std::cout << "Button added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Çalışma Sayfasına Satır Kontrolü Ekleme**

### **Microsoft Excel Kullanımı**

1. **Çizim** araç çubuğunda, **Şekiller**'e tıklayın, ardından **Satırlar**'a gelin ve istediğiniz çizgi stiline tıklayın.
1. Çizmek için sürükleyin.
1. Aşağıdakilerden birini veya her ikisinden birini yapın:
   1. Çizginin başlangıç noktasından 15 derece açılarla çizilmesini sınırlamak için, sürüklerken **SHIFT** tuşunu basılı tutun.
   1. İlk uç noktasından zıt yönlere doğru çizgiyi uzatmak için, sürüklerken **CTRL** tuşunu basılı tutun.

### **Aspose.Cells Kullanımı**

[**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) sınıfı, çalışma sayfasına çizgi şekli eklemek için [**AddLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addline/) adlı bir yöntem sağlar. Bu yöntem bir [**LineShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineshape/) nesnesi döndürür. [**LineShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineshape/) sınıfı, bir çizgiyi temsil eder. Bazı önemli üyeleri vardır:

- [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) yöntemi bir satırın formatını belirtir.
- [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) yöntemi, satırın hücrelere bağlandığı [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/) biçimini belirtir.

Aşağıdaki örnek, çalışma sayfasına satır eklemenin nasıl yapıldığını gösterir. Farklı stillerde üç satır oluşturur.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first worksheet in the book
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a new line to the worksheet
    LineShape line1 = worksheet.GetShapes().AddLine(5, 0, 1, 0, 0, 250);

    // Set the line dash style
    line1.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Set the placement
    line1.SetPlacement(PlacementType::FreeFloating);

    // Add another line to the worksheet
    LineShape line2 = worksheet.GetShapes().AddLine(7, 0, 1, 0, 85, 250);

    // Set the line dash style
    line2.GetLine().SetDashStyle(MsoLineDashStyle::DashLongDash);

    // Set the weight of the line
    line2.GetLine().SetWeight(4);

    // Set the placement
    line2.SetPlacement(PlacementType::FreeFloating);

    // Add the third line to the worksheet
    LineShape line3 = worksheet.GetShapes().AddLine(13, 0, 1, 0, 0, 250);

    // Set the line dash style
    line3.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Set the placement
    line3.SetPlacement(PlacementType::FreeFloating);

    // Make the gridlines invisible in the first worksheet
    worksheet.SetIsGridlinesVisible(false);

    // Save the excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Lines added successfully to the worksheet!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Bir ok başlığı eklemek**

Aspose.Cells, oklu satırlar çizmenize de olanak tanır. Bir satıra bir ok başlığı eklemek ve satırın biçimlendirilmesi mümkündür. Örneğin, satırın rengini değiştirebilir veya satırın ağırlığını ve stilini belirtebilirsiniz.

Aşağıdaki örnek, bir satıra bir ok başlığı eklemenin nasıl yapıldığını gösterir.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first worksheet in the book
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a line to the worksheet
    LineShape line2 = worksheet.GetShapes().AddLine(7, 0, 1, 0, 85, 250);

    // Set the line color
    line2.GetLine().SetFillType(FillType::Solid);
    line2.GetLine().GetSolidFill().SetColor(Color::Blue());

    // Set the weight of the line
    line2.GetLine().SetWeight(3);

    // Set the placement
    line2.SetPlacement(PlacementType::FreeFloating);

    // Set the line arrows
    line2.GetLine().SetEndArrowheadWidth(MsoArrowheadWidth::Medium);
    line2.GetLine().SetEndArrowheadStyle(MsoArrowheadStyle::Arrow);
    line2.GetLine().SetEndArrowheadLength(MsoArrowheadLength::Medium);
    line2.GetLine().SetBeginArrowheadStyle(MsoArrowheadStyle::ArrowDiamond);
    line2.GetLine().SetBeginArrowheadLength(MsoArrowheadLength::Medium);

    // Make the gridlines invisible in the first worksheet
    workbook.GetWorksheets().Get(0).SetIsGridlinesVisible(false);

    // Save the excel file
    workbook.Save(outDir + u"book1.out.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Çalışma Sayfasına Dikdörtgen Kontrolü Ekleme**

Aspose.Cells, çalışma sayfalarınızda dikdörtgen şekilleri çizmenize olanak tanır. Bir dikdörtgen, kare vb. oluşturabilirsiniz. Ayrıca kontrolün doldurma rengini, sınır çizgisi rengini biçimlendirmenize izin verilir. Örneğin, dikdörtgenin rengini değiştirebilir, gölgelendirme rengini ayarlayabilir veya dikdörtgenin ağırlığını ve stilini belirleyebilirsiniz.

### **Microsoft Excel Kullanımı**

1. **Çizim** araç çubuğunda, **Dikdörtgen**'e tıklayın.
1. Dikdörtgen çizmek için sürükleyin.
1. Aşağıdakilerden birini veya her ikisinden birini yapın:
   1. Dikdörtgeni başlangıç noktasından karesel çizmeyi kısıtlamak için sürükleme sırasında SHIFT tuşunu basılı tutun.
   1. Dikdörtgeni merkez noktasından çizmek için sürükleme sırasında CTRL tuşunu basılı tutun.

### **Aspose.Cells Kullanımı**

[**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) sınıfı, çalışma sayfasına bir dikdörtgen şekli eklemek için kullanılan [**AddRectangle**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addrectangle/) adında bir yöntem sağlar. Yöntem bir [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/rectangleshape/) nesnesi döndürür. [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/rectangleshape/) sınıfı bir dikdörtgeni temsil eder. Bazı önemli üyelere sahiptir:

- [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) özelliği bir dikdörtgenin satır formatı özelliklerini belirtir.
- [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) özelliği, dikdörtgenin çalışma sayfasındaki hücrelere bağlandığı [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/) biçimini belirtir.
- [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) özelliği bir dikdörtgenin doldurma biçimi stillerini belirtir.

Aşağıdaki örnek, bir dikdörtgenin çalışma sayfasına nasıl eklendiğini gösterir.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook excelbook;

    // Add a rectangle control to the first worksheet
    RectangleShape rectangle = excelbook.GetWorksheets().Get(0).GetShapes().AddRectangle(3, 0, 2, 0, 70, 130);

    // Set the placement of the rectangle
    rectangle.SetPlacement(PlacementType::FreeFloating);

    // Set the line weight
    rectangle.GetLine().SetWeight(4);

    // Set the dash style of the rectangle
    rectangle.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Save the Excel file
    excelbook.Save(outDir + u"book1.out.xls");

    std::cout << "Rectangle shape added and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Çalışma Sayfasına Yay Kontrolü Ekleme**

Aspose.Cells, çalışma sayfalarında yay şekilleri çizmenize olanak tanır. Basit ve dolu yaylar oluşturabilirsiniz. Kontrolün doldurma rengini ve sınır çizgisi rengini biçimlendirmenize izin verilir. Örneğin, yayın rengini belirleyebilir, gölgelendirme rengini ayarlayabilir veya şeklin ağırlığını ve stilini belirleyebilirsiniz.

### **Microsoft Excel Kullanımı**

1. **Çizim** araç çubuğunda, **Otomatik Şekiller** içinde **Yay**'e tıklayın.
1. Yay çizmek için sürükleyin.

### **Aspose.Cells Kullanımı**

[**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) sınıfı, çalışma sayfasına bir yay şekli eklemek için kullanılan [**AddArc**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addarc/) adında bir yöntem sağlar. Yöntem bir [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/arcshape/) nesnesi döndürür. [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/arcshape/) sınıfı bir yayı temsil eder. Bazı önemli üyelere sahiptir:

- [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) özelliği bir yayın satır formatı özelliklerini belirtir.
- [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) özelliği, yayın çalışma sayfasındaki hücrelere bağlandığı [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/) biçimini belirtir.
- [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) özelliği şeklin doldurma biçimi stillerini belirtir.
- [**GetLowerRightRow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightrow/) özelliği sağ alt köşe satır indisini belirtir.
- [**GetLowerRightColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightcolumn/) özelliği sağ alt köşe sütun indisini belirtir.

Aşağıdaki örnek, çalışma sayfasına yay şekilleri eklemenin nasıl yapıldığını göstermektedir. Örnek iki yay şekli oluşturur: biri doldurulmuş ve diğeri basit.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook excelbook;

    // Get the first worksheet
    Worksheet worksheet = excelbook.GetWorksheets().Get(0);

    // Add an arc shape
    ArcShape arc1 = worksheet.GetShapes().AddArc(2, 0, 2, 0, 130, 130);

    // Set the fill shape color
    arc1.GetFill().SetFillType(FillType::Solid);
    arc1.GetFill().GetSolidFill().SetColor(Color::Blue());

    // Set the placement of the arc
    arc1.SetPlacement(PlacementType::FreeFloating);

    // Set the line weight
    arc1.GetLine().SetWeight(1);

    // Set the dash style of the arc
    arc1.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Add another arc shape
    ArcShape arc2 = worksheet.GetShapes().AddArc(9, 0, 2, 0, 130, 130);

    // Set the line color
    arc2.GetLine().SetFillType(FillType::Solid);
    arc2.GetLine().GetSolidFill().SetColor(Color::Blue());

    // Set the placement of the arc
    arc2.SetPlacement(PlacementType::FreeFloating);

    // Set the line weight
    arc2.GetLine().SetWeight(1);

    // Set the dash style of the arc
    arc2.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Save the excel file
    U16String outputPath = outDir + u"book1.out.xls";
    excelbook.Save(outputPath);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Çalışma Sayfasına Oval Kontrolü Ekleme**

Aspose.Cells, çalışma sayfalarında oval şekilleri çizmenize olanak tanır. Basit ve dolu oval şekiller oluşturun ve kontrolün doldurma rengini ve kenar çizgisi rengini biçimlendirin. Örneğin, ovalin rengini belirleyebilir, gölgelendirme rengini ayarlayabilir, şeklin ağırlığını ve stilini belirleyebilirsiniz.

### **Microsoft Excel Kullanımı**

- *Çizim* araç çubuğunda, *Oval* a tıklayın.
- Oval çizmek için sürükleyin.
- Aşağıdakilerden birini veya her ikisini yapın:
- Ovalin başlangıç noktasından bir daire çizmek için sürükleme işlemini yaparken SHIFT tuşunu basılı tutun.
- Bir ovalı merkez noktasından çizmek için sürükleme işlemi yaparken CTRL tuşunu basılı tutun.

### **Aspose.Cells Kullanımı**

[**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) sınıfı, çalışma sayfasına oval bir şekil eklemek için kullanılan [**AddOval**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addoval/) adında bir yöntem sağlar. Yöntem, bir [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oval/) nesnesi döndürür. [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oval/) sınıfı bir oval şekli temsil eder. Bazı önemli üyelere sahiptir:

- [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) özelliği bir oval şeklin çizgi biçimi özniteliklerini belirtir.
- [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) özelliği, ovalin çalışma sayfasındaki hücrelere bağlandığı [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/) şeklini belirtir.
- [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) özelliği şeklin doldurma biçimi stillerini belirtir.
- [**GetLowerRightRow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightrow/) özelliği sağ alt köşe satır indisini belirtir.
- [**GetLowerRightColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightcolumn/) özelliği sağ alt köşe sütun indisini belirtir.

Aşağıdaki örnek, çalışma sayfasına oval şekiller eklemenin nasıl yapıldığını göstermektedir. Örnek iki oval şekli oluşturur: biri doldurulmuş oval diğeri basit daire.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook excelbook;

    // Add an oval shape
    Oval oval1 = excelbook.GetWorksheets().Get(0).GetShapes().AddOval(2, 0, 2, 0, 130, 160);

    // Set the placement of the oval
    oval1.SetPlacement(PlacementType::FreeFloating);

    // Set the line weight
    oval1.GetLine().SetWeight(1);

    // Set the dash style of the oval
    oval1.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Add another oval (circle) shape
    Oval oval2 = excelbook.GetWorksheets().Get(0).GetShapes().AddOval(9, 0, 2, 15, 130, 130);

    // Set the placement of the oval
    oval2.SetPlacement(PlacementType::FreeFloating);

    // Set the line weight
    oval2.GetLine().SetWeight(1);

    // Set the dash style of the oval
    oval2.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Save the excel file
    excelbook.Save(outDir + u"book1.out.xls");

    Aspose::Cells::Cleanup();
}
```

## **Çalışma Sayfasına Spinner Kontrolü Ekleme**

Bir spin kutusu, bir yukarı ok ve aşağı ok içeren bir düğmeye (spin düğmesi denir) bağlı bir metin kutusudur. Finansal modelinizde girdilerin değişiminin model çıktılarını nasıl değiştireceğini görebilirsiniz. Bir spin kutusunu belirli bir girdi hücresine bağlayabilirsiniz. Spin düğmesine tıkladığınızda, hedef girdi hücresindeki tam sayı değeri artar veya azalır. *Aspose.Cells*, çalışma sayfalarınızda spinner'lar oluşturmanıza olanak tanır.

### **Microsoft Excel Kullanımı**

Çalışma sayfanıza bir spin kutusu kontrolü yerleştirmek için:

- *Formlar* araç çubuğunun görüntülendiğinden emin olun.
- *Spinner* aracına tıklayın.
- Çalışma sayfanızdaki alanda, spinner'ı tutacak dikdörtgeni tanımlamak için tıklayın ve sürükleyin.
- Spinner çalışma sayfasına yerleştirildiğinde, kontrolün üzerine sağ tıklayın ve *Kontrolü Biçimlendir* i tıklayın ve maksimum, minimum ve artış değerlerini belirtin.
- *Bağlantı Hücresi* alanında, bu spin kutusunun bağlanması gereken hücrenin adresini belirtin.
- *Tamam* a tıklayın.

### **Aspose.Cells Kullanımı**

Sınıf [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/), bir çalışma sayfasına bir spin kutu denetimini eklemek için kullanılan [**AddSpinner**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addspinner/) adında bir yöntem sağlar. Yöntem bir [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/) nesnesi döndürür. [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/) sınıfı bir spin kutusunu temsil eder. Bazı önemli üyeleri vardır:

- [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) özelliği, spin kutusuyla bağlantılı bir hücreyi belirtir.
- [**GetMax()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getmax/) özelliği, spin kutusu aralığı için maksimum değeri belirtir.
- [**GetMin()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getmin/) özelliği, spin kutusu aralığı için minimum değeri belirtir.
- [**GetIncrementalChange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getincrementalchange/) özelliği, bir kaydırıcının bir satır kaydırılacak değer miktarını belirtir.
- [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getshadow/) özelliği, spin kutusunun 3B gölgeli olup olmadığını belirtir.
- [**GetCurrentValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getcurrentvalue/) özelliği, spin kutusunun geçerli değerini belirtir.

Aşağıdaki örnek, çalışma sayfasına bir spin kutusu eklemenin nasıl yapıldığını gösterir.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook excelbook;

    // Get the first worksheet
    Worksheet worksheet = excelbook.GetWorksheets().Get(0);

    // Get the worksheet cells
    Cells cells = worksheet.GetCells();

    // Input a string value into A1 cell
    cells.Get(u"A1").PutValue(u"Select Value:");

    // Set the font color of the cell
    Style styleA1 = cells.Get(u"A1").GetStyle();
    styleA1.GetFont().SetColor(Color::Red());

    // Set the font text bold
    styleA1.GetFont().SetIsBold(true);

    // Input value into A2 cell
    cells.Get(u"A2").PutValue(0);

    // Set the shading color to black with solid background
    Style styleA2 = cells.Get(u"A2").GetStyle();
    styleA2.SetForegroundColor(Color::Black());
    styleA2.SetPattern(BackgroundType::Solid);

    // Set the font color of the cell
    styleA2.GetFont().SetColor(Color::White());

    // Set the font text bold
    styleA2.GetFont().SetIsBold(true);

    // Add a spinner control
    Spinner spinner = worksheet.GetShapes().AddSpinner(1, 0, 1, 0, 20, 18);

    // Set the placement type of the spinner
    spinner.SetPlacement(PlacementType::FreeFloating);

    // Set the linked cell for the control
    spinner.SetLinkedCell(u"A2");

    // Set the maximum value
    spinner.SetMax(10);

    // Set the minimum value
    spinner.SetMin(0);

    // Set the incremental change for the control
    spinner.SetIncrementalChange(2);

    // Set it 3-D shading
    spinner.SetShadow(true);

    // Save the excel file
    excelbook.Save(outDir + u"book1.out.xls");

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Bir Çalışma Sayfasına Kaydırma Çubuğu Denetimi Ekleme**

Bir kaydırma çubuğu denetimi, bir çalışma sayfasında bir spin kutu denetimiyle benzer şekilde veri seçmeye yardımcı olmak için kullanılır. Denetimi bir çalışma sayfasına ekleyerek ve bir hücreye bağlayarak, denetimin mevcut konumunun sayısal bir değerini döndürmek mümkün olur.

### **Microsoft Excel Kullanımı**

- Excel 2003 ve daha önceki sürümlerde bir kaydırma çubuğu eklemek için, *Formlar* araç çubuğunda *Kaydırma Çubuğu* düğmesine tıklayın, ardından B2:B6 hücrelerini kaplayan ve sütunun genişliğinin yaklaşık dörtte biri uzunluğunda bir kaydırma çubuğu oluşturun.
- Excel 2007'de bir kaydırma çubuğu eklemek için *Geliştirici* sekmesine, ardından *Ekle* düğmesine ve ardından Form Kontrolleri bölümünde *Kaydırma Çubuğu*na tıklayın.
- Kaydırma çubuğuna sağ tıklayın ve ardından *Biçimlendirme Denetimi*ne tıklayın.
- Aşağıdaki bilgileri girin ve *Tamam* 'a tıklayın:
  - *Mevcut değer* kutusuna 1 yazın.
  - *Minimum değer* kutusuna 1 yazın. Bu değer, listedeki ilk öğenin üstünü kaydırma çubuğuna kısıtlar.
  - *Maksimum değer* kutusuna 20 yazın. Bu sayı, listedeki maksimum giriş sayısını belirtir.
  - *Artış değişikliği* kutusuna 1 yazın. Bu değer, kaydırma çubuğu denetimi mevcut değeri kaç sayı arttırırı belirler.
  - *Sayfa değişikliği* kutusuna 5 yazın. Bu giriş, kaydırma çubuğunda kaydırma kutusunun her iki tarafına tıklandığında mevcut değerin ne kadar artacağını kontrol eder.
  - Listenin seçilen öğesine bağlı olarak G1 hücresine bir sayı değeri koymak için, *Hücre bağlantısı* kutusuna G1 yazın.
- Kaydırma çubuğu seçilmediğinde herhangi bir hücreye tıklayın.

Kaydırma çubuğundaki yukarı veya aşağı kontrolüne tıkladığınızda, G1 hücresi, kaydırma çubuğunun artı veya eksi kaydırma çubuğu değişikliğinin mevcut değerini gösteren bir sayıya güncellenir.

### **Aspose.Cells Kullanımı**

Sınıf [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/), bir çalışma sayfasına bir kaydırma çubuğu denetimini eklemek için kullanılan [**AddScrollBar**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addscrollbar/) adında bir yöntem sağlar. Yöntem bir [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/) nesnesi döndürür. [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/) sınıfı bir kaydırma çubuğunu temsil eder. Bazı önemli üyeleri vardır:

- [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) özelliği, kaydırma çubuğuyla bağlantılı bir hücreyi belirtir.
- [**GetMax()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getmax/) özelliği, kaydırma çubuğu aralığı için maksimum değeri belirtir.
- [**GetMin()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getmin/) özelliği, kaydırma çubuğu aralığı için minimum değeri belirtir.
- [**GetIncrementalChange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getincrementalchange/) özelliği, bir kaydırmanın bir satır kaydırılacak değer miktarını belirtir.
- [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getshadow/) özelliği, bir kaydırma çubuğunun 3B gölgeli olup olmadığını belirtir.
- [**GetCurrentValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getcurrentvalue/) özelliği, kaydırma çubuğunun mevcut değerini belirtir.
- [**GetPageChange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getpagechange/) özelliği, kaydırma çubuğunun her iki yanına da tıklarsanız mevcut değerin ne kadar artırılacağını belirtir.

Aşağıdaki örnek, çalışma sayfasına bir kaydırma çubuğu nasıl ekleyeceğinizi gösterir.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook excelbook;

    // Get the first worksheet
    Worksheet worksheet = excelbook.GetWorksheets().Get(0);

    // Invisible the gridlines of the worksheet
    worksheet.SetIsGridlinesVisible(false);

    // Get the worksheet cells
    Cells cells = worksheet.GetCells();

    // Input a value into A1 cell
    cells.Get(u"A1").PutValue(1);

    // Set the font color of the cell
    cells.Get(u"A1").GetStyle().GetFont().SetColor(Color::Maroon());

    // Set the font text bold
    cells.Get(u"A1").GetStyle().GetFont().SetIsBold(true);

    // Set the number format
    cells.Get(u"A1").GetStyle().SetNumber(1);

    // Add a scrollbar control
    ScrollBar scrollbar = worksheet.GetShapes().AddScrollBar(0, 0, 1, 0, 125, 20);

    // Set the placement type of the scrollbar
    scrollbar.SetPlacement(PlacementType::FreeFloating);

    // Set the linked cell for the control
    scrollbar.SetLinkedCell(u"A1");

    // Set the maximum value
    scrollbar.SetMax(20);

    // Set the minimum value
    scrollbar.SetMin(1);

    // Set the incr. change for the control
    scrollbar.SetIncrementalChange(1);

    // Set the page change attribute
    scrollbar.SetPageChange(5);

    // Set it 3-D shading
    scrollbar.SetShadow(true);

    // Save the excel file
    excelbook.Save(outDir + u"book1.out.xls");

    std::cout << "Scrollbar added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Çalışma Sayfasındaki Grup Kontrollerine GroupBox Kontrolü Ekleme**

Bazen belirli bir gruba ait radyo düğmeleri veya diğer kontrolleri uygulamanız gerekebilir, bunu grup kutusu veya dikdörtgen kontrolünü dahil ederek uygulayabilirsiniz. Bu iki nesneden herhangi biri grup sınırlandırıcısı olarak hizmet eder. Bu şekillerden birini ekledikten sonra, ardından iki veya daha fazla radyo düğmesi veya diğer grup nesnelerini ekleyebilirsiniz.

### **Microsoft Excel Kullanımı**

Çalışma sayfanıza bir grup kutu kontrolü eklemek ve içine kontroller yerleştirmek için:

- Bir form başlatmak için ana menüde *Görünüm*ü, ardından *Araç Çubukları* ve *Formlar*ı tıklayın.
- *Formlar* araç çubuğunda, *Grup Kutu*nu tıklayın ve çalışma sayfasında bir dikdörtgen çizin.
- Kutu için bir başlık dizesi yazın.
- *Formlar* araç çubuğunda, *Seçenek Düğmesi*ne tıklayın ve başlık dizesinin hemen altına *Grup Kutusu*na tıklayın.
- *Formlar* araç çubuğunda tekrar *Seçenek Düğmesi*ne tıklayın ve önceki radyo düğmesinin altında *Grup Kutusu*na tıklayın.
- *Formlar* araç çubuğunda tekrar *Seçenek Düğmesi*ne tıklayın ve önceki radyo düğmesinin altında *Grup Kutusu*na tıklayın.

### **Aspose.Cells Kullanımı**

[**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) sınıfı, çalışma sayfasına bir grup kutu kontrolü eklemek için kullanılan [**AddGroupBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addgroupbox/) adında bir yöntem sağlar. Yöntem bir [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupbox/) nesnesi döndürür. Ayrıca, [**Group**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/group/) yöntemi, şekilleri gruplar, bu, bir [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) dizisi alır ve bir [**Shape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/) nesnesi döndürür. [**GroupShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupshape/) sınıfı bir grup kutusunu temsil eder. Önemli bazı üyelere sahiptir:

- [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) özelliği grup kutusunun başlık dizesini belirtir.
- [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupbox/getshadow/) özelliği grup kutusunun 3B gölgeleme olup olmadığını belirtir.

Aşağıdaki örnek, çalışma sayfasına bir grup kutu eklemeyi ve kontrolleri gruplamayı gösterir.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook excelbook;

    // Add a group box to the first worksheet
    Worksheet worksheet = excelbook.GetWorksheets().Get(0);
    GroupBox box = worksheet.GetShapes().AddGroupBox(1, 0, 1, 0, 300, 250);

    // Set the caption of the group box
    box.SetText(u"Age Groups");
    box.SetPlacement(PlacementType::FreeFloating);

    // Make it 2-D box
    box.SetShadow(false);

    // Add a radio button
    RadioButton radio1 = worksheet.GetShapes().AddRadioButton(3, 0, 2, 0, 30, 110);

    // Set its text string
    radio1.SetText(u"20-29");

    // Set A1 cell as a linked cell for the radio button
    radio1.SetLinkedCell(u"A1");

    // Make the radio button 3-D
    radio1.SetShadow(true);

    // Set the weight of the radio button
    radio1.GetLine().SetWeight(4);

    // Set the dash style of the radio button
    radio1.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Add another radio button
    RadioButton radio2 = worksheet.GetShapes().AddRadioButton(6, 0, 2, 0, 30, 110);

    // Set its text string
    radio2.SetText(u"30-39");

    // Set A1 cell as a linked cell for the radio button
    radio2.SetLinkedCell(u"A1");

    // Make the radio button 3-D
    radio2.SetShadow(true);

    // Set the weight of the radio button
    radio2.GetLine().SetWeight(4);

    // Set the dash style of the radio button
    radio2.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Add another radio button
    RadioButton radio3 = worksheet.GetShapes().AddRadioButton(9, 0, 2, 0, 30, 110);

    // Set its text string
    radio3.SetText(u"40-49");

    // Set A1 cell as a linked cell for the radio button
    radio3.SetLinkedCell(u"A1");

    // Make the radio button 3-D
    radio3.SetShadow(true);

    // Set the weight of the radio button
    radio3.GetLine().SetWeight(4);

    // Set the dash style of the radio button
    radio3.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Get the shapes
    Vector<Shape> shapeobjects{ box, radio1, radio2, radio3 };

    // Group the shapes
    GroupShape group = worksheet.GetShapes().Group(shapeobjects);

    // Save the excel file
    excelbook.Save(outDir + u"book1.out.xls");

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Gelişmiş Konular**
- [Aspose.Cells Kullanarak ActiveX Kontrolleri Ekleme](/cells/tr/cpp/add-activex-controls-using-aspose-cells/)
- [ActiveX Kontrolü Kaldırma](/cells/tr/cpp/remove-activex-control/)
- [ActiveX ComboBox Kontrolünü Güncelleme](/cells/tr/cpp/update-activex-combobox-control/)
