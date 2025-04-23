---
title: إدارة عناصر التحكم باستخدام ++C
linktitle: إدارة الضوابط
type: docs
weight: 150
url: /ar/cpp/managing-controls/
description: تعلم كيف تضيف وتدير عناصر تحكم متنوعة مثل الخطوط، المستطيلات، الأقواس، الدوائر، مؤشرات التشغيل، أشرطة التمرير، ومربعات المجموعة في أوراق العمل باستخدام Aspose.Cells مع ++C.
---

## **مقدمة**

يمكن للمطورين إضافة كائنات رسم مختلفة مثل صناديق النص، مربعات الاختيار، أزرار الراديو، مربعات التحرير، التسميات، الأزرار، الخطوط، المستطيلات، الأقواس، الدوائر، مؤشرات التشغيل، أشرطة التمرير، ومربعات المجموعة. توفر Aspose.Cells مساحة الأسماء `Aspose::Cells::Drawing` التي تحتوي على جميع كائنات الرسم. ومع ذلك، هناك بعض كائنات الرسم أو الأشكال التي لم يتم دعمها بعد. أنشئ هذه الكائنات في جدول تصميم بإستخدام Microsoft Excel ثم استورد الجدول المصمم إلى Aspose.Cells. تسمح لك Aspose.Cells بتحميل هذه الكائنات الرسومية من جدول تصميم وكتابتها إلى ملف مُولد.

## **إضافة مربع نص إلى ورقة العمل**

الطريقة الوحيدة لتوضيح المعلومات الهامة في تقرير هو استخدام صندوق نص. على سبيل المثال، إضافة نص لتسليط الضوء على اسم الشركة أو للإشارة إلى المنطقة الجغرافية التي تحقق أعلى مبيعات وما إلى ذلك. توفر Aspose.Cells الفئة [**TextBoxCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textboxcollection/)، المستخدمة لإضافة صندوق نص جديد إلى المجموعة. هناك فئة أخرى، [**TextBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textbox/)، التي تمثل صندوق نص يتم استخدامه لتحديد جميع أنواع الإعدادات. يحتوي على بعض الأعضاء الهامة:

- الخاصية [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) تُحدد نوع التوضع.
- الخاصية [**Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) تُحدد سمات الخط.
- الطريقة [**AddHyperlink**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/addhyperlink/) تضيف ارتباطًا تشعبيًا لصندوق النص.
- الخاصية [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) ترجع كائن [**MsoFillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/msofillformat/) يُستخدم لتعيين تنسيق التعبئة لصندوق النص.
- تُعيد الخاصية [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) كائن [**MsoLineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/msolineformat/) المستخدم عادة لتنسيق ووزن خط مربع النص.
- الخاصية [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) تحدد النص الذي يُدخل في صندوق النص.

المثال التالي ينشئ مربعي نص في الورقة العمل الأولى من الدفتر. المربع النص الأول مؤثث جيدًا بإعدادات تنسيق مختلفة. الثاني بسيط.

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

## **التحكم في صندوقات النص في جداول البيانات المصممة**

تتيح Aspose.Cells أيضًا لك الوصول إلى مربعات النص في جداول البيانات المصممة والتلاعب بها. استخدم الخاصية [**Worksheet.GetTextBoxes()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettextboxes/) للحصول على مجموعة مربعات النص في الورقة.

يستخدم المثال التالي ملف Microsoft Excel الذي أنشأناه في المثال أعلاه. يحصل على سلاسل نصيّة لصندوقي النص ويغير نص الصندوق الثاني لحفظ الملف.

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

## **إضافة عنصر تحكم خانة اختيار إلى ورقة العمل**

تكون مربعات الاختيار مفيدة إذا كنت ترغب في توفير طريقة للمستخدم لاختيار بين خيارين، مثل صحيح أو خطأ؛ نعم أو لا. تسمح Aspose.Cells لك باستخدام مربعات الاختيار في جداول البيانات. على سبيل المثال، قد تكون قد وضعت ورقة عمل للتنبؤ المالي يمكنك فيها إما أن تأخذ في الاعتبار استحواذ معين أو لا. في هذه الحالة، قد ترغب في وضع مربع اختيار في أعلى الورقة. يمكنك بعد ذلك ربط حالة هذا المربع بخلية أخرى، بحيث إذا تم تحديده، يكون قيمة الخلية صحيحة؛ إذا لم يتم تحديده، تكون قيمة الخلية خاطئة.

### **استخدام Microsoft Excel**

لوضع تحكم مربع الاختيار في ورقة العمل الخاصة بك، اتبع هذه الخطوات:

1. تأكد من عرض شريط الأدوات النماذج.
1. انقر على أداة **مربع اختيار** في شريط الأدوات النماذج.
1. في منطقة ورقة العمل الخاصة بك، انقر واسحب لتحديد المستطيل الذي سيحتوي على مربع الاختيار والتسمية بجانب مربع الاختيار.
1. بمجرد وضع مربع الاختيار، قم بتحريك مؤشر الماوس إلى منطقة التسمية وقم بتغيير التسمية.
1. في حقل **رابط الخلية**، حدد عنوان الخلية التي يجب ربط مربع الاختيار بها.
1. انقر فوق **موافق**.

### **استخدام Aspose.Cells**

توفر Aspose.Cells الفئة [**CheckBoxCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/checkboxcollection/) ، التي تُستخدم لإضافة مربع اختيار جديد إلى المجموعة. هناك فئة أخرى ، [**Aspose::Cells::Drawing::CheckBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/checkbox/) ، التي تمثل مربع اختيار. لديها بعض الأعضاء المهمين:

- تحدد خاصية [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) خلية مرتبطة بخانة الاختيار.
- تحدد خاصية [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) السلسلة النصية المرتبطة بخانة الاختيار. إنها تسمية خانة الاختيار.
- تحدد خاصية [**GetValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/checkbox/getvalue/) ما إذا كانت خانة الاختيار محددة أم لا.

يوضح المثال التالي كيفية إضافة خانة اختيار إلى ورقة العمل.

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

## **إضافة عنصر تحكم زر الراديو إلى ورقة العمل**

زر الراديو أو زر الخيار هو عنصر تحكم مكون من صندوق مستدير. يقوم المستخدم باتخاذ قراره عن طريق تحديد مربع المستدير. يتم عادةً ، إذا لم يكن دائمًا ، خيار زر الراديو مصحوبًا بآخرين. يظهر زر الراديو ويتصرف كمجموعة. يقرر المستخدم أي زر صالح عن طريق تحديد واحد فقط منها. عندما ينقر المستخدم على زر واحد ، يتم ملؤه. عند تحديد زر واحد في المجموعة ، تكون أزرار نفس المجموعة فارغة.

### **استخدام Microsoft Excel**

لوضع عنصر تحكم زر الراديو في ورقتك العمل ، اتبع هذه الخطوات:

1. تأكد من عرض شريط الأدوات **النماذج**.
1. انقر على أداة **Button الخيار**.
1. في ورقة العمل ، انقر واسحب لتحديد المستطيل الذي سيحتوي على زر الخيار والتسمية بجانب زر الخيار.
1. بمجرد وضع زر الراديو في ورقة العمل ، قم بتحريك مؤشر الماوس إلى منطقة التسمية وقم بتغيير التسمية.
1. في حقل **رابط الخلية** ، حدد عنوان الخلية التي يجب أن يكون مرتبطًا بها زر الراديو هذا.
1. انقر على **موافق**.

### **استخدام Aspose.Cells**

توفر فئة [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) طريقة تُسمى [**AddRadioButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addradiobutton/)، والتي تُستخدم لإضافة عنصر تحكم زر اختيار إلى ورقة العمل. تعيد الطريقة كائن [**Aspose::Cells::Drawing::RadioButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/radiobutton/). تمثل الفئة [**Aspose::Cells::Drawing::RadioButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/radiobutton/) زر الخيار. لها بعض الأعضاء المهمة:

- يُحدد خاصية [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) الخلية المرتبطة بزر الراديو.
- تُحدد خاصية [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) سلسلة النص المرتبطة بزر الراديو. إنها علامة زر الراديو.
- تُحدد خاصية [**IsChecked**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/radiobutton/ischecked/) ما إذا كان زر الراديو محددًا أم لا.
- تُحدد خاصية [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) تنسيق التعبئة لزر الراديو.
- تُحدد خاصية [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) أنماط تنسيق الخط لزر الخيار.

المثال التالي يوضح كيفية إضافة أزرار الراديو إلى ورقة العمل. يضيف المثال ثلاثة أزرار راديو تمثل مجموعات عمرية.

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

## **إضافة عنصر تحكم مربع القائمة المنسدلة إلى ورقة العمل**

لتسهيل إدخال البيانات، أو لتقييد الإدخالات إلى بعض العناصر التي تعرفها، يمكنك إنشاء مربع قائمة منسدلة، أو قائمة منسدلة للإدخالات الصحيحة التي تتم تجميعها من خلايا في مكان آخر على ورقة العمل. عند إنشاء قائمة منسدلة لخلية، تظهر سهم بجانب تلك الخلية. لإدخال معلومات في تلك الخلية، انقر على السهم، ثم انقر على الإدخال الذي تريده.

### **استخدام Microsoft Excel**

لوضع عنصر تحكم مربع الجمع في ورقة العمل الخاصة بك، اتبع هذه الخطوات:

1. تأكد من عرض شريط الأدوات **النماذج**.
1. انقر على أداة **مربع الجمع**.
1. في منطقة ورقة العمل الخاصة بك، انقر واسحب لتعريف المستطيل الذي سيحمل مربع الجمع.
1. بمجرد أن يتم وضع مربع الجمع في ورقة العمل، انقر بزر الماوس الأيمن على عنصر التحكم ثم انقر على **تنسيق التحكم** وحدد نطاق الإدخال.
1. في حقل **ارتباط الخلية**، حدد عنوان الخلية التي يجب ربطها بهذا مربع الجمع.
1. انقر فوق **موافق**.

### **استخدام Aspose.Cells**

توفر فئة [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) طريقة تحمل اسم [**AddComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addcombobox/)، والتي تُستخدم لإضافة عنصر تحكم مربع الجمع إلى ورقة العمل. تُعيد الطريقة كائن [**Aspose::Cells::Drawing::ComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/). الفئة [**Aspose::Cells::Drawing::ComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/) تمثل مربع جمع. لديها بعض الأعضاء المهمة:

- يحدد الخاصية [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) خلية مرتبطة بمربع الجمع.
- تحدد الخاصية [**GetInputRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getinputrange/) نطاق ورقة العمل للخلايا المستخدمة لملء مربع الجمع.
- تحدد الخاصية [**GetDropDownLines()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/getdropdownlines/) عدد خطوط القائمة المعروضة في الجزء المنسدل لمربع الجمع.
- تُشير الخاصية [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/getshadow/) ما إذا كان مربع الجمع له تظليل ثلاثي الأبعاد.

المثال التالي يوضح كيفية إضافة مربع الجمع إلى ورقة العمل.

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

## **إضافة عنصر تحكم تسمية إلى ورقة العمل**

التسميات هي وسيلة لتزويد المستخدمين بمعلومات حول محتويات جدول البيانات. يجعل Aspose.Cells من الممكن إضافة وتلاعب بالتسميات في ورقة العمل. توفر فئة [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) طريقة تحمل اسم [**AddLabel**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlabel/)، تستخدم لإضافة عنصر تحكم تسمية إلى ورقة العمل. تُعيد الطريقة كائن [**Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/). الفئة [**Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/) تمثل تسمية في ورقة العمل. لديها بعض الأعضاء المهمة:

- تحدد الطريقة [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) سلسلة تسمية التسمية.
- تحدد الطريقة [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/)، الطريقة التي يتم بها تثبيت التسمية على الخلايا في ورقة العمل.

المثال التالي يوضح كيفية إضافة تسمية إلى ورقة العمل.

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

## **إضافة عنصر تحكم مربع القائمة إلى ورقة العمل**

ينشئ عنصر تحكم مربع القائمة عنصر تحكم يسمح باختيار عنصر واحد أو عدة عناصر.

### **استخدام Microsoft Excel**

لوضع عنصر تحكم مربع القائمة في ورقة العمل:

1. تأكد من عرض شريط الأدوات **النماذج**.
1. انقر على أداة **مربع القائمة**.
1. في منطقة ورقة العمل الخاصة بك، انقر واسحب لتعريف المستطيل الذي سيحتوي على مربع القائمة.
1. بمجرد وضع مربع القائمة في ورقة العمل، انقر بزر الماوس الأيمن على العنصر التحكم للنقر فوق **تنسيق العنصر التحكم** وتحديد نطاق الإدخال.
1. في حقل **رابط الخلية**، حدد عنوان الخلية التي يجب أن يكون مربع القائمة مرتبطًا بها وتعيين نوع الاختيار (فردي، متعدد، توسيع) السمة
1. انقر على **موافق**.

### **استخدام Aspose.Cells**

توفر فئة [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) طريقة تُسمى [**AddListBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlistbox/)، والتي تُستخدم لإضافة عنصر تحكم مربع قائمة إلى ورقة العمل. تعيد الطريقة كائنًا [**Aspose::Cells::Drawing::ListBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/listbox/). تُمثل الفئة [**ListBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/listbox/) مربع قائمة. لها بعض الأعضاء الهامة:

- تحدد الطريقة [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) خلية مقترنة بمربع القائمة.
- تحدد الطريقة [**GetInputRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getinputrange/) نطاق ورقة العمل للخلايا المستخدمة لملء مربع القائمة.
- تحدد الطريقة [**SelectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/selectiontype/) وضع تحديد مربع القائمة.
- تُشير الطريقة [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/listbox/getshadow/) ما إذا كان لمربع القائمة تظليل ثلاثي الأبعاد.

يوضح المثال التالي كيفية إضافة مربع قائمة إلى ورقة العمل.

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

## **إضافة عنصر تحكم زر إلى ورقة العمل**

الأزرار مفيدة للقيام ببعض الإجراءات. في بعض الأحيان، من المفيد تعيين ماكرو VBA للزر أو تعيين ارتباط تشعبي لفتح صفحة ويب.

### **استخدام Microsoft Excel**

لوضع عنصر تحكم زر في ورقة العمل الخاصة بك:

1. تأكد من عرض شريط الأدوات **النماذج**.
1. انقر على أداة **الزر**.
1. في منطقة ورقة العمل الخاصة بك، انقر واسحب لتعريف المستطيل الذي سيحتوي على الزر.
1. بمجرد وضع مربع القائمة في ورقة العمل، انقر بزر الماوس الأيمن على العنصر التحكم واختر **تنسيق العنصر التحكم**، ثم حدد ماكرو VBA وسمات تتعلق بالخط، التوضيب، الحجم، الهامش وما إلى ذلك.
1. انقر فوق **موافق**.

### **استخدام Aspose.Cells**

الفئة [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) توفر طريقة تسمى [**AddButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addbutton/)، تستخدم لإضافة عنصر تحكم زر إلى ورقة العمل. تعيد الطريقة كائن [**Aspose::Cells::Drawing::Button**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/button/). الفئة [**Aspose::Cells::Drawing::Button**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/button/) تمثل زرًا. لديها بعض الأعضاء الهامة:

- الخاصية [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) تحدد التسمية للزر.
- الخاصية [**Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) تحدد سمات الخط لتسمية عنصر تحكم الزر.
- الخاصية [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) تحدد [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/)، الطريقة التي يتم بها ربط الزر بالخلايا في ورقة العمل.
- الخاصية [**AddHyperlink**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/addhyperlink/) تضيف ارتباطًا تشعبيًا لعنصر تحكم الزر. بالنقر على الزر، سيتم التنقل إلى عنوان URL ذي الصلة.

المثال التالي يوضح كيفية إضافة زر إلى ورقة العمل.

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

## **إضافة عنصر تحكم الخط إلى ورقة العمل**

### **استخدام Microsoft Excel**

1. على شريط الأدوات **الرسم**، انقر على **أشكال تلقائية**, اشير إلى **الخطوط**, واختر نمط الخط الذي تريده.
1. اسحب لرسم الخط.
1. قم بإحدى الخطوتين أو كليهما:
   1. لتقييد رسم الخط لزوايا 15 درجة من نقطته الأولى، اضغط باستمرار على SHIFT أثناء السحب.
   1. لتمديد الخط في اتجاهين معاكسين من نقطة النهاية الأولى، اضغط باستمرار على CTRL أثناء السحب.

### **استخدام Aspose.Cells**

تقدم فئة [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) طريقة تسمى [**AddLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addline/)، والتي تُستخدم لإضافة شكل خط إلى ورقة العمل. تعيد الطريقة كائن [**LineShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineshape/). تمثل الفئة [**LineShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineshape/) خطًا. لها بعض الأعضاء المهمة:

- تحدد الطريقة [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) تنسيق الخط.
- تحدد الطريقة [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) الـ [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/)، الطريقة التي يتم بها ربط الخط بالخلايا في ورقة العمل.

توضح الأمثلة التالية كيفية إضافة خطوط إلى ورقة العمل. يتم إنشاء ثلاث خطوط بأنماط مختلفة.

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

### **إضافة رأس سهم إلى خط**

تسمح Aspose.Cells أيضًا برسم خطوط سهم. من الممكن إضافة رأس سهم إلى خط وتنسيق الخط. على سبيل المثال، يمكنك تغيير لون الخط أو تحديد وزن ونمط الخط.

توضح الأمثلة التالية كيفية إضافة رأس سهم إلى خط.

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

## **إضافة تحكم مستطيل إلى ورقة عمل**

تسمح Aspose.Cells لك برسم أشكال مستطيلة في ورقة عملك. قد تقوم بإنشاء مستطيل، مربع وما إلى ذلك. كما يُسمح لك بتنسيق لون الملء ولون خط الحدود للتحكم. على سبيل المثال، يمكنك تغيير لون المستطيل، تحديد لون التظليل، تحديد وزن ونمط المستطيل حسب احتياجاتك.

### **استخدام Microsoft Excel**

1. في شريط الرسم، انقر فوق **المستطيل**.
1. اسحب لرسم المستطيل.
1. قم بإحدى الخطوتين أو كليهما:
   1. للقيد في رسم المستطيل لرسم مربع من نقطته البداية، اضغط باستمرار على SHIFT أثناء السحب.
   1. لرسم مستطيل من نقطة مركزية، اضغط باستمرار على CTRL أثناء السحب.

### **استخدام Aspose.Cells**

توفر فئة [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) طريقة تسمى [**AddRectangle**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addrectangle/)، التي تُستخدم لإضافة شكل مستطيل إلى ورقة عمل. تعيد الطريقة كائن [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/rectangleshape/). الفئة [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/rectangleshape/) تمثل مستطيلًا. لديها بعض الأعضاء الهامة:

- يحدد الخاصية [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) سمات تنسيق الخط لمستطيل.
- يحدد الخاصية [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) الـ [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/)، الطريقة التي يتم بها ربط المستطيل بالخلايا في ورقة العمل.
- الخاصية [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) تحدد أساليب تنسيق التعبئة الخاصة بمستطيل.

المثال التالي يظهر كيفية إضافة مستطيل إلى ورقة العمل.

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

## **إضافة تحكم بالقوس إلى ورقة العمل**

تسمح Aspose.Cells لك برسم أشكال القوس في ورقة العمل الخاصة بك. يمكنك إنشاء أقواس بسيطة وممتلئة. يُسمح لك بتنسيق لون التعبئة ولون الخط الحدودي للتحكم. على سبيل المثال، يمكنك تحديد / تغيير لون القوس، تحديد لون الظلال، تحديد الوزن والنمط للشكل حسب احتياجك.

### **استخدام Microsoft Excel**

1. على شريط الأدوات **الرسم**، انقر على **القوس** في **الأشكال التلقائية**.
1. اسحب لرسم القوس.

### **استخدام Aspose.Cells**

توفر الفئة [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) طريقة بعنوان [**AddArc**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addarc/)، والتي تُستخدم لإضافة شكل قوس إلى ورقة عمل. تُرجع الطريقة كائنًا من النوع [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/arcshape/). تُمثل الفئة [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/arcshape/) قوسًا. ولها بعض الأعضاء المهمة:

- الخاصية [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) تحدد سمات تنسيق الخط الخاصة بشكل القوس.
- الخاصية [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) تحدد [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/)، الطريقة التي يتم بها إرفاق القوس بالخلايا في ورقة العمل.
- خاصية [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) تحدد أنماط تنسيق التعبئة للشكل.
- تحدد خاصية [**GetLowerRightRow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightrow/) مؤشر الصف الأيمن الأدنى.
- تحدد خاصية [**GetLowerRightColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightcolumn/) مؤشر العمود الأيمن الأدنى.

المثال التالي يظهر كيفية إضافة أشكال قوسية إلى ورقة العمل. ينشئ المثال شكلين قوسيين: أحدهما ممتلئ والآخر بسيط.

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

## **إضافة تحكم بالشكل البيضوي إلى ورقة عمل**

تسمح Aspose.Cells لك برسم أشكال بيضوية في ورقات العمل. يمكنك إنشاء أشكال بيضوية بسيطة وممتلئة وتنسيق لون التعبئة ولون الخط الحدودي للتحكم. على سبيل المثال، يمكنك تحديد / تغيير لون الشكل البيضوي، تحديد لون الظلال، تحديد الوزن والنمط للشكل حسب احتياجك.

### **استخدام Microsoft Excel**

- على شريط الأدوات *الرسم*، انقر على *البيضوي*.
- اسحب لرسم البيضوي.
- قم بأحد أو كل من الآتي:
- لتقييد الشكل البيضاوي لرسم دائرة من نقطته البدء، اضغط على مفتاح SHIFT أثناء سحبه.
- لرسم شكل بيضاوي من نقطة مركزية، اضغط على CTRL أثناء سحبه.

### **استخدام Aspose.Cells**

تقدم فئة [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) طريقة تسمى [**AddOval**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addoval/)، التي تُستخدم لإضافة شكل بيضوي إلى ورقة العمل. تُرجع الطريقة كائن [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oval/). الفئة [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oval/) تمثل شكل بيضوي. لها بعض الأعضاء الهامة:

- تحدد خاصية [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) سمات تنسيق الخط لشكل بيضوي.
- خاصية [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) تحدد [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/)، الطريقة التي يتم فيها تعلق الشكل البيضاوي بالخلايا في ورقة العمل.
- خاصية [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) تحدد أنماط تنسيق التعبئة للشكل.
- تحدد خاصية [**GetLowerRightRow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightrow/) مؤشر الصف الأيمن الأدنى.
- تحدد خاصية [**GetLowerRightColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightcolumn/) مؤشر العمود الأيمن الأدنى.

المثال التالي يوضح كيفية إضافة أشكال بيضوية إلى ورقة العمل. ينشئ المثال شكلين بيضويين: أحدهما ممتلئ والآخر هو دائرة بسيطة.

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

## **إضافة عنصر تحكم Spinner إلى ورقة العمل**

مربع الدوران هو مربع نص مرتبط بزر (يسمى زر دوران) يتكون من سهمين لأعلى ولأسفل تنقر فوقهما لتغيير القيمة بشكل تدريجي في مربع النص. يمكنك من خلال استخدام مربعات الدوران أن ترى كيف تؤثر التغييرات في المدخلات على نموذجك المالي على إخراج النموذج. يمكنك ربط زر دوران بخلية مدخل معينة. أثناء النقر على زر الصعود أو النزول على زر الفاصل الزمني، تزداد قيمة العدد الصحيح في الخلية المدخل المستهدفة أو تنقص. *Aspose.Cells* يتيح لك إنشاء مربعات دوران في أوراق العمل الخاصة بك.

### **استخدام Microsoft Excel**

لوضع عنصر تحكم مربع الدوران في ورقة العمل الخاصة بك:

- تأكد من عرض شريط الأدوات *النماذج*.
- انقر فوق أداة *Spinner*.
- في منطقة ورقة العمل، انقر واسحب لتحديد المستطيل الذي سيحتوي على عنصر التحكم.
- بمجرد وضع عنصر التحكم في ورقة العمل، انقر بزر الفأرة الأيمن على العنصر التحكم وانقر على *تنسيق التحكم* وحدد القيم القصوى والصغرى والقيم التزايدية.
- في حقل *ارتباط الخلية*، حدد عنوان الخلية التي يجب أن يكون مربع الدوران مرتبط بها.
- انقر فوق *موافق*.

### **استخدام Aspose.Cells**

فئة [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) تُوفر طريقة تسمى [**AddSpinner**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addspinner/)، والتي تُستخدم لإضافة عنصر تحكم مربع دوراني إلى ورقة العمل. تُرجِع الطريقة كائن [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/). الفئة [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/) تمثل مربع دوراني. لديها بعض الأعضاء الهامة:

- يحدد الخاصية [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) الخلية المرتبطة بمربع الدوران.
- يحدد الخاصية [**GetMax()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getmax/) القيمة القصوى لنطاق مربع الدوران.
- يحدد الخاصية [**GetMin()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getmin/) القيمة الدنيا لنطاق مربع الدوران.
- يحدد الخاصية [**GetIncrementalChange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getincrementalchange/) كمية القيمة التي يتم زيادتها عند التمرير بخطوة واحدة.
- تشير الخاصية [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getshadow/) ما إذا كان مربع الدوران يحتوي على تظليل ثلاثي الأبعاد.
- يحدد الخاصية [**GetCurrentValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getcurrentvalue/) القيمة الحالية لمربع الدوران.

المثال التالي يوضح كيفية إضافة مربع دوراني إلى ورقة العمل.

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

## **إضافة عنصر تحكم شريط التمرير إلى ورقة العمل**

يُستخدم عنصر التحكم بشريط التمرير لمساعدة في تحديد البيانات على ورقة العمل بشكل مماثل لعنصر تحكم مربع الدوران. من خلال إضافة العنصر التحكم إلى ورقة العمل وربطه بخلية، يكون من الممكن العودة بقيمة رقمية للموضع الحالي للعنصر التحكم.

### **استخدام Microsoft Excel**

- لإضافة شريط تمرير في Excel 2003 والإصدارات السابقة، انقر فوق زر *شريط التمرير* على شريط الأدوات *النماذج*، ثم أنشئ شريط تمرير يغطي الخلايا B2:B6 في الارتفاع ويكون بنسبة رُبع عرض العمود.
- لإضافة شريط تمرير في Excel 2007، انقر فوق علامة *المطور*، ثم انقر على *إدراج*، ومن ثم انقر على *شريط التمرير* في قسم عناصر النماذج.
- انقر بزر الماوس الأيمن على شريط التمرير، ومن ثم انقر فوق *تنسيق الضبط*.
- اكتب المعلومات التالية، وانقر فوق *موافق*:
  - في مربع القيمة الحالية، اكتب 1.
  - في مربع القيمة الدنيا، اكتب 1. يحدد هذا القيمة الحد الأقصى لشريط التمرير لأول عنصر في القائمة.
  - في مربع القيمة القصوى، اكتب 20. تُحدد هذه الرقم الحد الأقصى لعدد الإدخالات في القائمة.
  - في مربع التغيير التدريجي، اكتب 1. تحكم هذه القيمة في كم عدد الأرقام التي يزيد بها تحكم شريط التمرير القيمة الحالية.
  - في مربع تغيير الصفحة، اكتب 5. تحكم هذا الإدخال في مقدار زيادة القيمة الحالية إذا نقرت داخل شريط التمرير على أي جانب من جوانب المربع التمرير.
  - لوضع قيمة رقمية في الخلية G1 (تبعًا للعنصر المحدد في القائمة)، اكتب G1 في مربع الرابط الخلوي.
- انقر فوق أي خلية بحيث لا يتم تحديد شريط التمرير.

عندما تنقر فوق التحكم بتحريك لأعلى أو لأسفل على شريط التمرير، يتم تحديث الخلية G1 إلى الرقم الذي يشير إلى القيمة الحالية لشريط التمرير بالإضافة إلى أو ناقص تغيير التحكم التدريجي لشريط التمرير.

### **استخدام Aspose.Cells**

يوفر الفصيلة [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) طريقة تُدعى [**AddScrollBar**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addscrollbar/)، والتي تُستخدم لإضافة تحكم شريط التمرير إلى ورقة العمل. تُرجع الطريقة كائن [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/). الفصيلة [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/) تُمثل تحكم شريط التمرير. لها بعض الأعضاء المهمة:

- تحدد الخاصية [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) الخلية المرتبطة بشريط التمرير.
- تحدد الخاصية [**GetMax()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getmax/) القيمة القصوى لنطاق شريط التمرير.
- تحدد الخاصية [**GetMin()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getmin/) القيمة الدنيا لنطاق شريط التمرير.
- تحدد الخاصية [**GetIncrementalChange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getincrementalchange/) مقدار القيمة الذي يتم به زيادة شريط التمرير بتمريرة.
- توضح الخاصية [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getshadow/) ما إذا كان لشريط التمرير تظليل ثلاثي الأبعاد أم لا.
- تحدد الخاصية [**GetCurrentValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getcurrentvalue/) القيمة الحالية لشريط التمرير.
- تحدد الخاصية [**GetPageChange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getpagechange/) مقدار زيادة القيمة الحالية إذا نقرت داخل شريط التمرير على أي جانب من جوانب المربع التمرير.

المثال التالي يظهر كيفية إضافة شريط تمرير إلى ورقة العمل.

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

## **إضافة تحكم مجموعة إلى تحكمات المجموعة في ورقة عمل**

في بعض الأحيان قد تحتاج إلى تنفيذ أزرار الراديو أو تحكمات أخرى تنتمي إلى مجموعة معينة، يمكنك تنفيذ ذلك من خلال تضمين إما مربع مجموعة أو تحكم مستطيل. يمكن لأي من هاتين الشكلين أن يكون محدد المجموعة. بعد إضافة أحد هاتين الشكلين، يمكنك بعد ذلك إضافة اثنين أو أكثر من أزرار الراديو أو أجهزة مجموعة أخرى.

### **استخدام Microsoft Excel**

لوضع تحكم مربع المجموعة في ورقة العمل الخاصة بك ووضع تحكمات فيه:

- لبدء النموذج، على القائمة الرئيسية، انقر فوق *عرض*، ثم *شرائط الأدوات*، ثم *نماذج*.
- في شريط الأدوات *النماذج*، انقر فوق *مربع التجميع* وارسم مستطيلًا على ورقة العمل.
- اكتب سلسلة تسمية للمربع.
- في شريط أدوات *النماذج*، انقر فوق *زر الاختيار* وانقر داخل *مربع التجميع* مباشرة تحت سلسلة التسمية.
- من شريط الأدوات *النماذج* مرة أخرى، انقر *زر الاختيار* وانقر داخل *مربع التجميع* تحت الزر الإشعاري الأول.
- مرة أخرى على شريط الأدوات *النماذج*، انقر فوق *زر الاختيار* وانقر داخل *مربع التجميع* تحت الزر الإشعاري السابق.

### **استخدام Aspose.Cells**

توفر فئة [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) الأسلوب المسمى [**AddGroupBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addgroupbox/)، والذي يُستخدم لإضافة عنصر تحكم مربع تجميع إلى ورقة العمل. يُرجع الأسلوب كائن [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupbox/). علاوة على ذلك، فإن الأسلوب [**Group**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/group/) لفئة [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) يجمع بين الأشكال، حيث يأخذ مصفوفة [**Shape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/) كمعلمة ويُرجع كائن [**GroupShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupshape/). تمثل الفئة [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupbox/) مربع تجميع. تحتوي على بعض الأعضاء المهمة:

- تحدد الخاصية [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) سلسة تسمية مربع التجميع.
- تشير الخاصية [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupbox/getshadow/) ما إذا كان مربع التجميع لديه تظليل ثلاثي الأبعاد.

المثال التالي يُظهر كيفية إضافة مربع تجميع وتجميع عناصر التحكم في ورقة العمل.

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

## **مواضيع متقدمة**
- [إضافة عناصر تحكم ActiveX باستخدام Aspose.Cells](/cells/ar/cpp/add-activex-controls-using-aspose-cells/)
- [إزالة عنصر تحكم ActiveX](/cells/ar/cpp/remove-activex-control/)
- [تحديث عنصر تحكم ActiveX ComboBox](/cells/ar/cpp/update-activex-combobox-control/)
