---  
title: Microsoft Excel İleri Filtresini Kullanarak Karmaşık Kriterleri Karşılayan Kayıtları Göstermek
type: docs  
weight: 280  
url: /tr/nodejs-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/  
description: Microsoft Excel’in gelişmiş filtre uygulamasını kullanarak karmaşık kriterleri karşılayan kayıtları göstermek için Aspose.Cells for Node.js via C++ API yi kullanmayı öğrenin.  
keywords: Node.js ile Gelişmiş Filtre Uygula C++, aracılığıyla Node.js Gelişmiş Filtreyi ayarla C++, Node.js ile Gelişmiş Filtre Ekle C++, Node.js ile Gelişmiş Filtre Oluştur C++, Gelişmiş filtreyi bir aralığa nasıl eklerim Node.js C++ kullanarak  
---  

## **Olası Kullanım Senaryoları**  

Microsoft Excel, karmaşık kriterleri karşılayan kayıtları göstermek için çalışma sayfası verilerinde *Gelişmiş Filtre* uygulamanıza olanak tanır. Gelişmiş Filtre'yi *Veri > Gelişmiş* komutu ile uygulayabilirsiniz, ekran görüntüsünde gösterildiği gibi.  

![todo:image_alt_text](1.png)  

Aspose.Cells for Node.js via C++ ayrıca [**Worksheet.advanced_Filter()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#advanced_Filter-boolean-string-string-string-boolean-) yöntemini kullanarak Gelişmiş Filtreyi uygulamanıza olanak tanır. Microsoft Excel'e benzer şekilde, aşağıdaki parametreleri kabul eder.  

**isFilter**  

Listeyi yerinde filtrelemenin belirtilip belirtilmediğini gösterir.  

**listRange**  

Liste aralığı.  

**criteriaRange**  

Kriter aralığı.  

**copyTo**  

Verilerin kopyalanacağı aralık.  

**uniqueRecordOnly**  

Yalnızca benzersiz satırların gösterimi veya kopyalanması.  

## **Karmaşık Kriterleri Karşılayan Kayıtları Göstermek İçin Microsoft Excel'in İleri Filtresini Uygulayın**  

Aşağıdaki örnek kod, [Örnek Excel Dosyası](48496692.xlsx) üzerinde gelişmiş filtreyi uygular ve [Çıktı Excel Dosyası](48496691.xlsx) oluşturur. Ekran görüntüsü her iki dosyayı karşılaştırmak için gösterir. Ekran görüntüsü içindekileri incelediğinizde, verilerin karmaşık kriterlere göre çıktı Excel dosyası içinde filtrelendiğini görebilirsiniz.  

![todo:image_alt_text](2.png)  

## **Örnek Kod**  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-AdvancedFilter.js" >}}


{{< app/cells/assistant language="nodejs-cpp" >}}
