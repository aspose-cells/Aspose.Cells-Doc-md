---
title: التحقق مما إذا كان مشروع VBA محميًا ومغلقًا للمشاهد باستخدام Node.js عبر C++
linktitle: التحقق مما إذا كان مشروع VBA محميًا ومقفلا للعرض
type: docs
weight: 30
url: /ar/nodejs-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/
description: تعلم كيفية التحقق مما إذا كان مشروع VBA في ملف Excel محميًا ومغلقًا للمشاهد باستخدام Aspose.Cells for Node.js via C++.
---

## التحقق مما إذا كان مشروع VBA محميًا ومغلقًا للمشاهد في Node.js

يسمح Aspose.Cells بالتحقق مما إذا كان مشروع VBA لملف Excel محميًا ومقفلًا للمراجعة. لهذا، يوفر API الخاصية [**VbaProject.getIslockedForViewing()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#getIslockedForViewing--). إذا كانت مغلقة للمراجعة، فإن الخاصية [**VbaProject.getIslockedForViewing()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#getIslockedForViewing--) تُرجع **true**.

## **الكود المثالي**

 يحمل نموذج الكود التالي ملف Excel النموذجي ([ملف Excel النموذجي](43352065.xlsm)) ويتحقق مما إذا كان مشروع VBA (برمجة Visual Basic للتطبيقات) الخاص بملف Excel محميًا ومغلقًا للمشاهدة. يرجى مراجعة خرج وحدة التحكم للمرجعية.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source Excel file.
const filePath = path.join(dataDir, "sampleCheckifVBAProjectisProtected.xlsm");
const workbook = new AsposeCells.Workbook(filePath);

// Access the VBA project of the workbook.
const vbaProject = workbook.getVbaProject();

// Whether "Lock project for viewing" is true or not.
console.log("Is VBA Project Locked for Viewing: " + vbaProject.getIslockedForViewing());
```

## **مخرجات الوحدة**

هذا هو مخرج الكونسول للكود العيني أعلاه عند تنفيذه مع [ملف Excel عيني](43352065.xlsm) المقدم.

{{< highlight java >}}

Is VBA Project Locked for Viewing: True

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
