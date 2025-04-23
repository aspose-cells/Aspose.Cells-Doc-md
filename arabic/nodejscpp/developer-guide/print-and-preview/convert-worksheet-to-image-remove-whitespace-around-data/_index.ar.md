---
title: تحويل ورقة العمل إلى صورة  إزالة الفراغ حول البيانات باستخدام Node.js عبر C++
linktitle: تحويل ورقة عمل إلى صورة  إزالة الفراغات حول البيانات
type: docs
weight: 40
url: /ar/nodejs-cpp/convert-worksheet-to-image-remove-whitespace-around-data/
description: تعلم كيفية تحويل أوراق عمل Microsoft Excel إلى صور وإزالة المساحات الفارغة حول البيانات باستخدام Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

أحيانًا، قد تحتاج إلى عرض صور ورق العمل في التطبيقات أو صفحات الويب. على سبيل المثال، قد تحتاج إلى إدراج صور في مستند Word، ملف PDF، عرض PowerPoint، أو مستند آخر. بشكل أساسي، ترغب في عرض ورقة العمل كصورة بحيث يمكن لصقها في تطبيقات أخرى. تُسمح لك Aspose.Cells بتحويل جداول بيانات Microsoft Excel إلى صور.

{{% /alert %}}

## **إزالة الفراغات حول البيانات**

[**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender) API يحول ورقة عمل إلى ملف صورة مع أي سمات محددة، على سبيل المثال، تنسيق الصورة، الصفحات المقسمة، وما إلى ذلك. تدعم عدة صيغ للصور، بما في ذلك BMP، GIF، JPG، TIFF، و EMF.

عند استخدام ميزة الورقة إلى الصورة، يكون للصورة الناتجة فراغ حولها تلقائياً. يمكنك إزالة ذلك عن طريق تعيين الهوامش العلوية، السفلية، اليسرى واليمنى لتوجيه صفحة ورقة المصدر إلى 0 وتحديد [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions) بشكل مناسب.

الكود التالي يزيل الفراغات حول البيانات في الصورة الناتجة.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);
const options = new AsposeCells.LoadOptions();
options.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All));
// Specify your print area if you want
// sheet.getPageSetup().setPrintArea("A1:H8");

// To remove the white border around the image.
sheet.getPageSetup().setLeftMargin(0);
sheet.getPageSetup().setRightMargin(0);
sheet.getPageSetup().setBottomMargin(0);
sheet.getPageSetup().setTopMargin(0);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();
imgOptions.setImageType(AsposeCells.ImageType.Emf);

// Set only one page would be rendered for the image
imgOptions.setOnePagePerSheet(true);
imgOptions.setPrintingPage(AsposeCells.PrintingPageType.IgnoreBlank);

// Create the SheetRender object based on the sheet with its ImageOrPrintOptions attributes
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Convert the image
sr.toImage(0, path.join(outputDir, "outputRemoveWhitespaceAroundData.emf"));
```
