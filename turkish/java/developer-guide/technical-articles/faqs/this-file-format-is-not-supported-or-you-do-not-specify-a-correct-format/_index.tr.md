---
title: Bu dosya biçimi desteklenmiyor veya doğru bir biçim belirtmediniz
type: docs
weight: 10
url: /tr/java/this-file-format-is-not-supported-or-you-do-not-specify-a-correct-format/
---

## **Bu dosya formatı desteklenmiyor veya doğru bir biçim belirtmediniz**
Kullanıcı şablon dosyasından çalışma kitapları oluştururken dosya biçimini belirtmişse, genellikle bu hata belirtilen dosya biçiminin şablon dosyasının gerçek dosya biçimi olmamasından kaynaklanır. Kullanıcı dosya biçimini belirtmemişse, genellikle bu durum dosya ad uzantısının dosyanın gerçek biçimini yansıtmaması ve otomatik olarak tespit edilememesi nedeniyle olur, örneğin herhangi bir özel tanımlayıcı olmayan csv/tsv dosyası. Elbette, Cells tarafından desteklenmeyen dosya biçimleri de bu hatayı rapor eder.
{{< app/cells/assistant language="java" >}}
