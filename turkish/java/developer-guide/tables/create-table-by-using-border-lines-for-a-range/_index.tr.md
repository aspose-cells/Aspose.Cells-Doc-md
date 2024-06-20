---
title: Bir Veri Aralığı için Kenar Çizgileri Kullanarak Tablo Oluşturma
type: docs
weight: 50
url: /tr/java/create-table-by-using-border-lines-for-a-range/
description: Kenar çizgilerini kullanarak bir veri aralığına tablo oluşturmanın nasıl yapıldığını gösterir. Aspose.Cells for Java, bir aralığa kenarlıklar eklemek için kullanılabilecek kullanımı kolay bir API sağlar.
keywords: tablo oluştur, aralık tabloya, aralık tabloya excel, excel aralık tabloya, kenar çizgileri olan aralıktan tabloya, aralıktan tablo oluşturma, aralığı tabloya dönüştürme, excel aralığı tabloya dönüştürme, excel tablo oluşturma, aralıktan tabloya java 
---

{{% alert color="primary" %}}

Bazen, sahip olduğunuz hücrelerin adresine dayalı olarak bir **Aralık**/**Hücre Alanı** içinden kenar çizgileri ekleyerek bir tablo oluşturmak isteyebilirsiniz. Bir hücre aralığı oluşturmak için [**Cells.createRange**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange(int,%20int,%20boolean)) yöntemini kullanabilirsiniz. [**Cells.createRange**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange(int,%20int,%20boolean)) yöntemi bir [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range) nesnesi döndürür. [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) nesnesi oluşturabilir ve sınır çizgilerini (üst, sol, alt, sağ) seçeneklerine göre belirleyebilirsiniz. Daha sonra [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range) hücrelerini alabilir ve istediğiniz biçimlendirmeyi uygulayabilirsiniz.

{{% /alert %}}

Aşağıdaki örnek, bir [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range) oluşturmayı ve aralık hücreleri için kenar çizgilerini belirlemeyi göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateTableforRange-CreateTableforRange.java" >}}

Yukarıdaki kodu çalıştırdıktan sonra, biçimlendirilmiş bir tablo içeren oluşturulmuş excel dosyasına sahip olabiliriz; işte dosyanın ekran görüntüsü.

![todo:image_alt_text](create-table-by-using-border-lines-for-a-range_1.png)
