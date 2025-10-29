---  
title: الحصول على أو تعيين معرف الفئة لكائن OLE المدمج باستخدام Node.js عبر C++  
linktitle: الحصول على أو تعيين معرف الفئة لكائن Ole المضمن  
type: docs  
weight: 200  
url: /ar/nodejs-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/  
description: تعلم كيفية الحصول على أو تعيين معرف فئة كائنات OLE المضمنة في Node.js باستخدام Aspose.Cells عبر C++.  
---  

## **سيناريوهات الاستخدام المحتملة**  
يوفر Aspose.Cells الخاصية [OleObject.getClassIdentifier()](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getClassIdentifier--) والتي يمكنك استخدامها للحصول على أو تعيين معرف فئة كائن OLE المضمّن. معرفات فئة كائن OLE هي في الواقع GUIDs، أي معرفات فريدة عالمياً. دائماً ما يكون GUID بطول 16 بايت؛ لذلك، فإن معرفات الفئات أيضاً بطول 16 بايت. غالبًا ما توجد داخل سجل Windows وتوفر معلومات لتطبيق المضيف حول كيفية فتح الكائنات OLE المضمنة التي تحتوي على موارد مضمّنة داخل تطبيق العميل.

## **الحصول على معرف الفئة الخاص بكائن OLE المضمّن أو تعيينه**  
يُظهر لقطه الشاشة التالية معرف فئة كائن الـ OLE أي GUID الذي تم قراءته من [ملف إكسل النموذجي](5115190.xls) الذي يحتوي على كائن PowerPoint مدمج داخل OLE.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)  
### **الكود المثالي**  
يرجى الاطلاع على رمز النموذج التالي الذي تم تنفيذه باستخدام [ملف إكسل النموذجي](5115190.xls) وإخراجه عبر وحدة التحكم التي تطبع معرف فئة الكائن OLE أي GUID. GUID المطبوع هو بالضبط نفسه كما هو موضح داخل لقطة الشاشة.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your sample workbook which contains embedded PowerPoint ole object
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xls"));

// Access its first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first ole object inside the worksheet
const oleObject = worksheet.getOleObjects().get(0);

// Convert 16-bytes array into GUID
const guid = new Uint8Array(oleObject.getClassIdentifier()).reduce((acc, byte) => acc + String.fromCharCode(byte), '');

// Print the GUID
console.log(guid.toUpperCase());
```  
### **مخرجات الوحدة**  
هذه هي مخرجات وحدة التحكم للرمز النموذجي أعلاه عند تنفيذه باستخدام [ملف إكسل النموذجي](5115190.xls).

{{< highlight java >}}  
 DC020317-E6E2-4A62-B9FA-B3EFE16626F4  
{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
