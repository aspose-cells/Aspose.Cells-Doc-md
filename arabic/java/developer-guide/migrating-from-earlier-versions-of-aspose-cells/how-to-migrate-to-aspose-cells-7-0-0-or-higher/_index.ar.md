---
title: كيفية الانتقال إلى Aspose.Cells 7.0.0 أو أحدث
type: docs
weight: 10
url: /ar/java/how-to-migrate-to-aspose-cells-7-0-0-or-higher/
---

{{% alert color="primary" %}}

في هذا المقال، قمنا بمشاركة التغييرات الملحوظة في واجهة برمجة التطبيقات التي تم إجراؤها في Aspose.Cells for Java 7.0.0 والإصدارات اللاحقة مقارنة بالإصدارات السابقة من Aspose.Cells for Java. سيساعد هذا المقال المستخدمين على ترحيل السريع من الواجهة البرمجية القديمة إلى الواجهة البرمجية الجديدة من خلال فهم التغييرات التي تم إجراؤها وتنفيذها في تطبيقاتهم.

{{% /alert %}}

## **التغييرات الملحوظة للمستخدمين الحاليين**

منذ إصدار Aspose.Cells for Java v7.0.0 ، قمنا بتعديلات رئيسية في واجهة برمجة التطبيقات وأضفنا كل تلك الميزات الموجودة في Aspose.Cells for .NET حتى الآن. لذا ، ستكون كلاً من Aspose.Cells for Java و.NET مقارنة الآن من حيث الميزات وحتى من حيث أسماء الأساليب والخصائص.

بالمثل للنهج القديم ، يمكنك فقط استيراد بيان واحد فقط في تطبيقك لاسترداد جميع الفئات والواجهات وما إلى ذلك.

[**Java**]

{{< highlight java >}}

 import com.aspose.cells.*;

{{< /highlight >}}

لقد قمنا بإعادة تسمية بعض مجموعة واجهات برمجة التطبيقات لتنظيف بنية واجهة برمجة التطبيقات لمطابقتها مع Aspose.Cells for .NET. لقد أضفنا بعض فئات المجموعات الآن وقمنا بتبديلها مع فئات المجموعات الحالية. على سبيل المثال ، تم استبدال فئة Worksheets بـ **WorksheetCollection**. بالمثل ، تم استبدال فئة Shapes بـ **ShapeCollection**. ومع ذلك ، لم تتأثر وظائف الفئات بل تم تعزيزها بالفعل.

إذا كنت ترغب في ترحيل إلى واجهة برمجة التطبيقات الجديدة ، فيجب أن تقوم بإجراء التغييرات التالية في تطبيقك لجعل الأمور تعمل من جانبك. القائمة التالية تحتوي على التغييرات التي تم إجراؤها في الفئات وأساليبها المتناظرة.

## **ملخص التغييرات في واجهة برمجة التطبيقات**

1) تمت إعادة تسمية المجموعات في v2.5.4 أو الإصدارات السابقة التي تنتهي باسم 's'. في v7.0.0 أو الإصدارات الأحدث ، يتم تسمية المجموعات على النحو التالي:
مثال: Shapes (قديم) -> ShapeCollection (جديد) ، Worksheets (قديم) -> WorksheetCollection (جديد) ، ... الخ.

2) تغير استرجاع العنصر من المجموعة. على سبيل المثال ، في v2.5.4 أو الإصدارات السابقة كنا نفعله كـ getXXX(int) ، في v7.0.0 أو الإصدارات الأحدث ، نفعله الآن كـ get(int):
مثال: Worksheets.getSheet(int) (قديم) -> WorksheetCollection.get(int) (جديد) ، ... الخ.

3) تغيير الحصول على حجم (عدد العناصر) لإحدى المجموعات. في v2.5.4 أو الإصدارات السابقة ، كنا نقوم بذلك باستخدام size() ، في v7.0.0 أو الإصدارات الأحدث ، نقوم الآن بذلك باستخدام getCount():
مثال: Worksheets.size() (قديم) -> WorksheetCollection.getCount() (جديد) ، ... الخ.

4) تم تغيير أسماء طرق الحصول على الخصائص البوليانية في v2.5.4 أو الإصدارات السابقة التي تبدأ بـ 'is'. في v7.0.0 يتم بدء هذه بـ "get":
مثال: PageSetup.isBlackAndWhite() (قديم) -> PageSetup.getBlackAndWhite() (جديد) ، ... الخ.
{{< app/cells/assistant language="java" >}}
