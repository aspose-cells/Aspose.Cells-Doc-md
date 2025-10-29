---
title: تعيين رؤوس وتذييلات مع C++
linktitle: ضبط رؤوس وأسافل
type: docs
weight: 30
url: /ar/cpp/setting-headers-and-footers/
description: تشرح هذه المقالة كيفية إدراج صورة برمجياً في رأس وتذييل أوراق عمل Excel من خلال تعيين الرأس والتذييل باستخدام أوامر السكربت عبر واجهة برمجة تطبيقات أو مكتبة C++.
keywords: إدراج صورة في رأس وتذييل Excel باستخدام C++، تعيين أوامر السكربت ل الرأس والتذييل في Excel باستخدام C++
---

{{% alert color="primary" %}}

رؤوس وأسافل هي سطور النص المعروضة أسفل هامش الأعلى أو أعلى الهامش على التوالي. يمكن إضافة رؤوس وأسافل إلى الأوراق العمل أيضًا. يمكن استخدام رؤوس وأسافل لعرض معلومات مفيدة مثل رقم الصفحة أو اسم المؤلف أو اسم الموضوع أو التاريخ والوقت. يتم إدارة الرؤوس والأسافل باستخدام إعدادات تخطيط الصفحة.

{{% /alert %}}

## **ضبط رؤساء الصفحات وتذايلها**

يتيح Aspose.Cells لك إضافة رؤوس وتذييلات للصفحات بناءً على النموذج أو الإعداد الذي تم تصميمه مسبقًا للطباعة، ولكنها موصى بها يدوياً. يمكنك استخدام Microsoft Excel كأداة لواجهة رسومية (GUI) لتعيين رؤوس وتذييلات لتوفير الجهد والوقت في التطوير. يمكن ل Aspose.Cells استيراد الملف وحفظ الإعدادات.

لإضافة رؤوس وتذييلات بناءً على النموذج، يوفر Aspose.Cells استدعاءات API خاصة وأوامر سكريبت لتنسيق الرؤوس والتذييلات.

### **أوامر السكريبت**

أوامر السكريبت هي أوامر خاصة تسمح لك بتعيين تنسيقات الرأس والتذييل.

| **أوامر السكريبت** | **الوصف** |
| :- | :- |
|&P| - رقم الصفحة الحالية
|&G| - صورة
|&N| - مجموع عدد الصفحات
|&D| - التاريخ الحالي
|&T| - الوقت الحالي
|&A| - اسم ورقة العمل
|&F| - اسم الملف بدون مساره
|&&Text|يعرض &Text. على سبيل المثال: &&WO سيتم عرضه كـ &WO|
|&"\<FontName>"| - يمثل اسم الخط. على سبيل المثال: &"Arial"
|&"\<FontName>, \<FontStyle>"| - يمثل اسم الخط بالنمط. مثال: &"Arial,Bold"
|&\<FontSize>| - يمثل حجم الخط. على سبيل المثال: “&14abc”. ولكن، إذا تبعت هذه الأمر برقم عادي يتم طباعته في الرأس، يجب أن يتم فصله بحرف مسافة عن حجم الخط. على سبيل المثال: “&14 123”.

### **تعيين رؤوس وتذييلات**

يوفر [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) فئتين، [**SetHeader**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setheader/) و [**SetFooter**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setfooter/)، تُستخدم لإضافة رأس وتذيل لورقة عمل. هذه الفئات تأخذ فقط معلمتين:

- **القسم** – القسم الذي يجب وضع الرأس أو التذيل فيه. هناك ثلاثة أقسام: اليسار، الوسط، واليمين، يُمثلون بالترتيب 0، 1، و2.
- **السكريبت** – السكريبت الذي يجب استخدامه للرأس أو التذيل. يتضمن هذا السكريبت أوامر سكريبت لتنسيق الرؤوس أو التذيلات.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook excel;

    // Get the first worksheet's PageSetup
    PageSetup pageSetup = excel.GetWorksheets().Get(0).GetPageSetup();

    // Set worksheet name at the left section of the header
    pageSetup.SetHeader(0, u"&A");

    // Set current date and time at the central section of the header with custom font
    pageSetup.SetHeader(1, u"&\"Times New Roman,Bold\"&D-&T");

    // Set current file name at the right section of the header with custom font
    pageSetup.SetHeader(2, u"&\"Times New Roman,Bold\"&12&F");

    // Set a string at the left section of the footer with custom font for part of the string
    pageSetup.SetFooter(0, u"Hello World! &\"Courier New\"&14 123");

    // Set the current page number at the central section of the footer
    pageSetup.SetFooter(1, u"&P");

    // Set page count at the right section of the footer
    pageSetup.SetFooter(2, u"&N");

    // Save the workbook
    excel.Save(u"SetHeadersAndFooters_out.xls");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **إدراج صورة في رأس أو تذيل**

يوجد في الفئة [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) طريقتان إضافيتان، [**SetHeaderPicture**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setheaderpicture/) و [**SetFooterPicture**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setfooterpicture/)، تُستخدم لإضافة الصور إلى الرأس والتذييل. تأخذ هذه الطرق المعاملات التالية:

- **القسم** – القسم الخطوط العليا أو السفلية حيث سيتم وضع الصورة. هناك ثلاثة أقسام، اليمين، الوسط واليسار، يُمثلها القيم 0، 1 و 2 على التوالي.
- **مصفوفة بايت** – البيانات الرسومية (يجب كتابة البيانات الثنائية في مخزن مصفوفة بايت).

بعد تنفيذ الكود أدناه وفتح الملف، تحقق من رأس الصفحة في ورقة العمل عن طريق:

1. في قائمة **ملف**, حدد **إعداد الصفحة**. سيتم عرض مربع حواري.
1. حدد علامة التبويب **رأس / تذييل**.

```cpp
#include <iostream>
#include <fstream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Creating a Workbook object
    Workbook workbook;

    // Creating a string variable to store the url of the logo/picture
    U16String logo_url = srcDir + u"aspose-logo.jpg";

    // Declaring a FileStream object
    ifstream inFile;

    // Declaring a byte array
    vector<uint8_t> binaryData;

    // Opening the logo/picture in the stream
    inFile.open(logo_url.ToUtf8(), ios::binary);

    if (inFile.is_open())
    {
        // Get the size of the file
        inFile.seekg(0, ios::end);
        size_t fileSize = inFile.tellg();
        inFile.seekg(0, ios::beg);

        // Resize the byte array to the size of the file
        binaryData.resize(fileSize);

        // Read the file into the byte array
        inFile.read(reinterpret_cast<char*>(binaryData.data()), fileSize);

        // Creating a PageSetup object to get the page settings of the first worksheet of the workbook
        PageSetup pageSetup = workbook.GetWorksheets().Get(0).GetPageSetup();

        // Convert std::vector to Aspose::Cells::Vector
        Aspose::Cells::Vector<uint8_t> asposeBinaryData(binaryData.data(), static_cast<int32_t>(binaryData.size()));

        // Setting the logo/picture in the central section of the page header
        pageSetup.SetHeaderPicture(1, asposeBinaryData);

        // Setting the script for the logo/picture
        pageSetup.SetHeader(1, u"&G");

        // Setting the Sheet's name in the right section of the page header with the script
        pageSetup.SetHeader(2, u"&A");

        // Saving the workbook
        workbook.Save(outDir + u"InsertImageInHeaderFooter_out.xls");

        // Closing the FileStream object
        inFile.close();
    }
    else
    {
        cerr << "Failed to open the image file." << endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
