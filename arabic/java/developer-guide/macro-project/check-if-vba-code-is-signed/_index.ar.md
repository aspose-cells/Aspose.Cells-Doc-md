---
title: تحقق مما إذا كان رمز VBA قد تم توقيعه
type: docs
weight: 30
url: /ar/java/check-if-vba-code-is-signed/
---
{{% alert color="primary" %}}

 Aspose.Cells يسمح للمستخدم بالتحقق مما إذا كان مشروع كود VBA موقعاً أم لا. الرجاء استخدام[**Workbook.getVbaProject (). isSigned ()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned) طريقة للتحقق مما إذا كان مشروع رمز VBA موقّعًا أم لا.

{{% /alert %}}

## **تحقق مما إذا كان رمز VBA قد تم توقيعه**

 يشرح الكود التالي كيفية التحقق مما إذا كان رمز VBA موقّعًا أم لا يستخدم ملف[**Workbook.getVbaProject (). isSigned ()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned) طريقة. يمكنك استخدام أي من ملفات Excel الخاصة بك لاختبار هذا الرمز. لغرض الاختبار يمكنك استخدامه[ملف Excel هذا المستخدم في الكود](5472500.xlsm).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckVBAProjectInWorkbookIsSigned-CheckVBAProjectInWorkbookIsSigned.java" >}}

## **إخراج وحدة التحكم**

 أدناه هو إخراج وحدة التحكم من الكود أعلاه باستخدام[نموذج ملف اكسل](5472500.xlsm) المقدمة من الرابط.

{{< highlight "java" >}}

Is VBA Code Project Signed: true

{{< /highlight >}}
