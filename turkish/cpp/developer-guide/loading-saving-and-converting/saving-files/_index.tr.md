---
title: Dosyaları Kaydetme
type: docs
weight: 20
url: /tr/cpp/saving-files/
---
{{% alert color="primary" %}} 

Aspose.Cells, dosya oluşturmayı ve kaydetmeyi ve mevcut dosyaları değiştirmeyi mümkün kılar. Bu makalede dosyaların kaydedilebileceği çeşitli yollar açıklanmaktadır.

{{% /alert %}} 
##  **Dosyaları Kaydetmenin Farklı Yolları**
 Aspose.Cells şunları sağlar[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Microsoft Excel dosyasını temsil eder ve Excel dosyalarıyla çalışmak için gerekli yöntemleri sağlar.[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıf şunları sağlar[Kaydetmek](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) Excel dosyalarını kaydetmek için kullanılan yöntem.[Kaydetmek](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) yöntemi, dosyaları farklı şekillerde kaydetmek için kullanılan birçok aşırı yüklemeye sahiptir. Dosyanın kaydedileceği dosya formatına,[Formatı Kaydet](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)numaralandırma.
##  **Dosyayı Bazı Konumlara Kaydetme**
Dosyaları bir depolama konumuna kaydetmek için, dosya adını (depolama yolu ile birlikte) ve istediğiniz dosya biçimini ([Formatı Kaydet](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) numaralandırma) çağırırken[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) nesnenin[Kaydetmek](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)yöntem.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToSomeLocation-new.cpp" >}}


##  **Dosyayı Akışa Kaydetme**
 Dosyaları bir akışa kaydetmek için bir MemoryStream veya FileStream nesnesi oluşturun ve dosyayı çağırarak bu akış nesnesine kaydedin.[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) nesnenin[Kaydetmek](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) yöntem. kullanarak istediğiniz dosya formatını belirtin.[Formatı Kaydet](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) çağırırken numaralandırma[Kaydetmek](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)yöntem.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToStream-new.cpp" >}}
