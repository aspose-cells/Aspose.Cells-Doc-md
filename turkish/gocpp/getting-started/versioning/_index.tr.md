---
title: Sürümleme
type: docs
weight: 40
url: /tr/go-cpp/versioning/
description: Aspose Cells for Go yu C++ ile nasıl kurulur ve Merhaba Dünya uygulaması nasıl yapılır.
---

**github.com/aspose-cells/aspose-cells-go-cpp/v25** Üçüncü taraf kütüphanesinin belirli bir sürümünü belirten bir Go modül yoludur. Bu modül yolunun anlamını açıklayalım:
Modül Yolunu Çözümleme

1. **GitHub Depo Adresi**: github.com/aspose-cells/aspose-cells-go-cpp

- Bu bölüm, kütüphanenin GitHub üzerinde, aspose-cells organizasyonu veya kullanıcısı altında, aspose-cells-go-cpp adlı depoda barındırıldığını gösterir.
- Aspose.Cells, elektronik tablo dosyalarını işleme ve düzenleme için API setidir (Excel gibi).

1. **Sürüm Numarası**: /v25

- /v25, bu kütüphanenin 24. sürüm olduğunu gösterir. Go Modüllerinde, semantik sürümleme (SemVer) desteklenmektedir ve /vN içeren yollar, ana sürüm numarasını açıkça belirtmek için kullanılır.
- Ana sürüm 2 veya daha büyükse, uyumluluğu sağlamak ve farklı ana sürümlerin izolasyonunu korumak için modül yoluna sürüm numarası eklenmelidir.

### **Anlamı**

- **aspose-cells-go-cpp**: Bu, C++ kütüphanesi için Go dil bağlamıdır ve Aspose.Cells fonksiyonlarını Go programlarınızda kullanmanıza olanak tanır; Excel dosyalarını okuma, yazma ve düzenleme dahil olmak üzere çeşitli işlemler yapabilirsiniz.
- **v25**: Bu, kütüphanenin 24. sürümüne referans verdiğinizi gösterir. Farklı ana sürümler uyumsuz değişiklikler getirebilir, bu nedenle sürüm numarasını belirtmek, projenizin doğru API ve davranışa bağlı kalmasını sağlar.

### **Kullanım**

Go projenizde aspose-cells-go-cpp v25 kullanmak için, aşağıdaki satırı projelerinizin go.mod dosyasına eklemeniz gerekir:

```Go
require github.com/aspose-cells/aspose-cells-go-cpp/v25 v25.x.x
```

v25.x.x yerine, örneğin v25.0.0 gibi belirli küçük ve yama sürüm numaralarını kullanın. Bu bağımlılığı otomatik olarak eklemek ve indirmek için go get komutunu kullanabilirsiniz:

```Go
go get github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.x.x
```
