---
title: Güvenlik İstisnası Sorunu
type: docs
weight: 30
url: /tr/net/security-exception-issue/
---

## **Güvenlik İstisnası Sorunu**
Bazı kullanıcılar Aspose.Cells'ı kullanmaya çalışırken "Güvenlik İstisnası" hatası alabilir. Bu sorun genellikle bir web uygulamasında meydana gelir.
### **Açıklama**
Aspose.Cells'in bazı önemli özellikleri sağlamak için **Win32 GDI API'lerini** çağırması gerekebilir. Web sunucusunun katı bir güven seviyesine sahip olması durumunda bu güvenlik istisnası fırlatılabilir.
### **Çözüm**
Lütfen Aspose.Cells.dll'e "Yönetilmeyen derlemelere çağrılara izin ver" seçeneği etkinleştirilmiş bir yeni izin kümesi oluşturmayı deneyin.
{{< app/cells/assistant language="csharp" >}}
