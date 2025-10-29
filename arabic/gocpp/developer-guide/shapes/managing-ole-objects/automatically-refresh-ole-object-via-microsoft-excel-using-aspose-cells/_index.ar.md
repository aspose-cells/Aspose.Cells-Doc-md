---
title: تحديث الكائن OLE تلقائيًا عبر Microsoft Excel باستخدام جولانج عبر C++
linktitle: تحديث تلقائي لكائن OLE
type: docs
weight: 270
url: /ar/go-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
description: تعلم كيفية تحديث الكائنات OLE تلقائيًا في Microsoft Excel باستخدام Aspose.Cells مع جولانج عبر C++
---

{{% alert color="primary" %}}

توفر Aspose.Cells الخاصية [**OleObject.GetAutoLoad()**](https://reference.aspose.com/cells/go-cpp/oleobject/getautoload/) لتحديث كائن OLE عند فتح ملف إكسل في Microsoft Excel. بفضل هذه الخاصية، ستعرض صورة OLE الصحيحة التي أنشأها Microsoft Excel.

{{% /alert %}}

الكود النموذجي التالي يحمل [ملف إكسل النموذجي](5115231.xlsx) الذي يحتوي على صورة OLE غير حقيقية. في الواقع، كائن OLE هو مستند Microsoft Word، لكن ملف إكسل النموذجي يعرض صورة الحيوان بدلاً من صورة Microsoft Word. ومع ذلك، إذا فتحت ملف إكسل الناتج ([5115225.xlsx](#))، ستلاحظ أن Microsoft Excel يعرض صورة OLE الصحيحة.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AutomaticallyRefreshOleObjectViaMicrosoftExcelUsingAsposeCells.go" >}}
