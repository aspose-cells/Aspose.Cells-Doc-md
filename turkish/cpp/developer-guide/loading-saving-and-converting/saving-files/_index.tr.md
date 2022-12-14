---
title: Dosyaları Kaydetme
type: docs
weight: 20
url: /tr/cpp/saving-files/
---
{{% alert color="primary" %}} 

Aspose.Cells, dosya oluşturmayı ve kaydetmeyi ve mevcut dosyaları değiştirmeyi mümkün kılar. Bu makalede, dosyaların kaydedilebileceği çeşitli yollar açıklanmaktadır.

{{% /alert %}} 
## **Dosyaları Kaydetmenin Farklı Yolları**
 Aspose.Cells şunları sağlar:[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) Microsoft Excel dosyasını temsil eden ve Excel dosyalarıyla çalışmak için gerekli yöntemleri sağlayan. bu[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)sınıf sağlar[Kaydetmek](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349) Excel dosyalarını kaydetmek için kullanılan yöntem. bu[Kaydetmek](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349) yöntem, dosyaları farklı şekillerde kaydetmek için kullanılan birçok aşırı yüklemeye sahiptir. Dosyanın kaydedileceği dosya biçimi, kullanıcı tarafından belirlenir.[Biçimi Kaydet](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a)numaralandırma.
## **Dosyayı Bir Konuma Kaydetmek**
 Dosyaları bir depolama konumuna kaydetmek için, dosya adını (depolama yolu ile birlikte) ve istenen dosya biçimini (ilk dosyadan) belirtin.[Biçimi Kaydet](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a) numaralandırma) çağrılırken[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) nesnenin[Kaydetmek](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)yöntem.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToSomeLocation.cpp" >}}


## **Dosyayı Akışa Kaydetme**
 Dosyaları bir akışa kaydetmek için bir MemoryStream veya FileStream nesnesi oluşturun ve dosyayı çağırarak bu akış nesnesine kaydedin.[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) nesnenin[Kaydetmek](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349) yöntem. kullanarak istenen dosya biçimini belirtin.[Biçimi Kaydet](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a) çağrılırken numaralandırma[Kaydetmek](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)yöntem.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToStream.cpp" >}}
