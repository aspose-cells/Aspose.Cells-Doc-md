---
title: تحديث كائن Ole تلقائيًا عبر Microsoft Excel باستخدام Aspose.Cells
type: docs
weight: 270
url: /ar/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
---

{{% alert color="primary" %}}

يوفر Aspose.Cells خاصية [**OleObject.AutoLoad**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/autoload) لتحديث كائن OLE عند فتح ملف الإكسل في Microsoft Excel. نتيجة لهذه الخاصية، سيعرض الكائن OLE الصورة الصحيحة المُولدة بواسطة Microsoft Excel.

{{% /alert %}}

يقوم الكود العينة التالي بتحميل [ملف الإكسل العينة](5115231.xlsx) الذي يحتوي على صورة OLE غير حقيقية. الكائن OLE هو في الواقع مستند Microsoft Word ولكن ملف الإكسل العينة يعرض صورة الحيوان بدلاً من صورة Microsoft Word. ولكن إذا فتحت [ملف الإكسل الناتج](5115225.xlsx)، سترى Microsoft Excel عرض الصورة الصحيحة لـ OLE.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-RefreshOLEObjects-1.cs" >}}
