---
title: Güvenlik İstisnası Sorunu
type: docs
weight: 30
url: /tr/net/security-exception-issue/
---
## **Güvenlik İstisnası Sorunu**
Bazı kullanıcılar Aspose.Cells'i kullanmaya çalışırken "Güvenlik İstisnası" hatası alabilirler. Bu sorun genellikle bir web uygulamasında meydana gelir.
### **Açıklama**
 Aspose.Cells biraz aramak zorunda**Win32 GDI API'leri** bazı önemli özellikler sağlamak için. Web sunucusunun katı bir güven düzeyi varsa, bu güvenlik istisnası atılabilir.
### **Çözüm**
Lütfen "Yönetilmeyen derlemelere yapılan çağrılara izin ver" etkinken Aspose.Cells.dll güvenlik izni vermek için yeni bir izin seti oluşturmaya çalışın.
