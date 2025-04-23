---  
title: تحديث الأيام مع الحفاظ على سجل تاريخ المراجعات في المصنف المشترك باستخدام Node.js عبر C++  
linktitle: تحديث الأيام الحفظ تاريخ سجلات المراجعة في الورقة المشتركة  
type: docs  
weight: 80  
url: /ar/nodejs-cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/  
description: تعلم كيفية تحديث عدد الأيام للحفاظ على سجل مراجعة التاريخ في المصنفات المشتركة باستخدام Aspose.Cells for Node.js via C++.  
---  

## **سيناريوهات الاستخدام المحتملة**

عند مشاركة مصنف، تحصل على خيار يقول ***احتفظ بسجل التغييرات لمدة N أيام*** كما هو موضح في لقطة الشاشة التالية. يمكنك تحديث عدد الأيام للحفاظ على السجل باستخدام Aspose.Cells for Node.js via C++ مع الخاصية [**WorksheetCollection.getDaysPreservingHistory()**](https://reference.aspose.com/cells/nodejs-cpp/revisionlogcollection/#getDaysPreservingHistory--).

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **تحديث أيام الاحتفاظ بتاريخ سجل المراجعة في دفتر العمل المشترك**

الكود المثالي التالي يقوم بإنشاء دفتر عمل فارغ، ثم يشاركه ويحدّث أيام سجلات المراجعة للحفاظ على التاريخ لـ 7 أيام والتي تكون عادة 30 يومًا. يُرجى الرجوع إلى [ملف الإكسل الناتج](60489773.xlsx) الذي تم إنشاؤه بواسطة الكود للرجوع إليه.

## **الكود المثالي**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Create empty workbook
const workbook = new AsposeCells.Workbook();

// Share the workbook
workbook.getSettings().setShared(true);

// Update DaysPreservingHistory of RevisionLogs
workbook.getWorksheets().getRevisionLogs().setDaysPreservingHistory(7);

// Save the workbook
workbook.save("outputShared_DaysPreservingHistory.xlsx");
```  

