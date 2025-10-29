---
title: إلغاء تثبيت الصفوف أو الأعمدة مع Node.js عبر C++
linktitle: إلغاء تجميد الأجزاء
type: docs
weight: 190
url: /ar/nodejs-cpp/unfreeze-rows-or-columns-of-excel-worksheet
description: في هذا المقال، ستتعلم كيفية إلغاء تثبيت الصفوف والأعمدة أو الألواح في أوراق عمل Excel برمجياً باستخدام واجهة برمجة تطبيقات Node.js مع C++.
keywords: إلغاء تثبيت الألواح، إلغاء تثبيت الصفوف، إلغاء تثبيت الأعمدة، unFreeze النافذة عبر Node.js باستخدام C++.
---

## **مقدمة**

في هذا المقال، سنتعلم كيفية إلغاء تثبيت الصفوف والأعمدة والألواح. إذا كانت أوراق عمل في ملفات Excel مجمدة، أحيانًا نرغب في إلغاء تجميد الورقة أو تعديل الصفوف والأعمدة أو الألواح المجمدة.


## **في إكسل**

1. انقر على علامة التبويب عرض > تجميد الألواح > إلغاء تجميد الألواح.

**![إلغاء تجميد الألواح في إكسل](Unfreeze-Panes.png)**




## **إلغاء تثبيت الصفوف أو الأعمدة أو الألواح مع Aspose.Cells for Node.js via C++**
من السهل إلغاء تثبيت الألواح باستخدام Aspose.Cells for Node.js via C++. يرجى استخدام طريقة [**Worksheet.unFreezePanes()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unFreezePanes--) لإلغاء تثبيت الألواح.

1. إنشاء ورقة عمل لفتح الملف المجمد.
2. إلغاء تثبيت الألواح باستخدام طريقة Worksheet.unfreezePanes()
3. حفظ الملف.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const frozenFilePath = path.join(dataDir, "Frozen.xlsx");

const workbook = new AsposeCells.Workbook(frozenFilePath); 
workbook.getWorksheets().get(0).unFreezePanes();
workbook.save("Unfrozen.xlsx");
```

المرفق [ملف إكسل عيني](Frozen.xlsx).
{{< app/cells/assistant language="nodejs-cpp" >}}
