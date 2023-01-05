---
title: مشكلة HTTPS SSL
type: docs
weight: 20
url: /ar/net/https-ssl-issue/
---
## **مشكلة HTTPS / SSL**
أبلغ بعض المستخدمين أنهم واجهوا مشاكل في تنزيل ملفات Excel التي تم إنشاؤها باستخدام Aspose.Cells. عند فتح مربع حوار الحفظ ، يحتوي اسم الملف على اسم صفحة aspx بدلاً من ملف Excel ، ويكون نوع الملف فارغًا.
### **خاطئة**
قمنا بتغيير رؤوس استجابة HTTP لحل مشكلة ضغط HTTP. قد يتسبب هذا في مشكلة أثناء إرسال الملفات إلى مستعرض العميل من خلال HTTPS / SSL.
### **المحلول**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPSSSLIssue.aspx-SSLIssue.cs" >}}
