---
title: Java 20.2 Sürüm Notları aracılığıyla PHP için Aspose.Cells
type: docs
weight: 10
url: /tr/php-java/aspose-cells-for-php-via-java-20-2-release-notes/
---
{{% alert color="primary" %}} 

Bu sayfa, Java 20.2 üzerinden PHP için Aspose.Cells sürüm notlarını içerir.

{{% /alert %}} 

|**Anahtar**|**Özet**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-43076|İşlenen HTML dosyasında görüntü türü EMF'yi ayarlayın|Artırma|
|CELLSJAVA-43113|PDF'ye dönüştürme - java.lang.NumberFormatException: Giriş dizesi için|Artırma|
|CELLSJAVA-43114|PDF'ye dönüştürme - Geçersiz formül:"'APRIL''12'.A1:'APRIL''12'.I23"|Artırma|
|CELLSJAVA-43117|PDF'ye dönüştürme - onaltılık geçerli bir onaltılık sayı değil|Artırma|
|CELLSJAVA-43118|PDF'ye dönüştürme - java.lang.NumberFormatException: Giriş dizesi için: "341.403.811.74"|Artırma|
|CELLSJAVA-43077|Çalışma sayfası HTML'ye dönüştürülürken ortaya çıkan "Beklenmeyen görüntü türü" istisnası|Böcek|
|CELLSJAVA-43096|Excel dosyası HTML'ye dönüştürülürken program kilitleniyor|Böcek|
|CELLSJAVA-43107|PDF'ye Dönüştürme - com.aspose.cells.CellsException: Şekilden resme Hata!|Böcek|
|CELLSJAVA-43108|PDF'ye dönüştürme - com.aspose.cells.CellsException|Böcek|
|CELLSJAVA-43088|Radar grafiği, XLSX'ten PDF'e dönüştürmede çıktı dosyasında işlenmez|Böcek|
|CELLSJAVA-43091|Donut grafiğindeki veri etiketleri PDF dosyasında çakışıyor|Böcek|
|CELLSJAVA-43099|Çalışma sayfası görüntüsü düzgün şekilde oluşturulmuyor|Böcek|
|CELLSJAVA-43093|ActiveX denetimi, XLS dosya biçiminde algılanmıyor|Böcek|
|CELLSJAVA-43104|getShowTabs ve setShowTabs ile ilgili sorunlar|Böcek|
|CELLSJAVA-43121|OOM, XLS'de sayfa sayısını almaya çalışıyor|Böcek|
|CELLSJAVA-43125|Form ve ActiveX nesneleri çoğaltılır|Böcek|
|CELLSJAVA-43094|XLSX dosya formatı yüklenirken istisna|İstisna|
|CELLSJAVA-43100|Bir Excel dosyasında Workbook.calculateFormula() çağrılırken "java.lang.ArrayIndexOutOfBoundsException" istisnası|İstisna|
|CELLSJAVA-43123|MEMORY_PREFERENCE kullanılırken ArrayIndexOutOfBoundsException|İstisna|
|CELLSJAVA-43105|PDF'ye dönüştürme - java.lang.ArrayIndexOutOfBoundsException: 60|İstisna|
|CELLSJAVA-43106|PDF'ye dönüştürme - java.lang.IllegalArgumentException|İstisna|
|CELLSJAVA-43109|PDF'ye dönüştürme - java.lang.NullPointerException|İstisna|
|CELLSJAVA-43111|PDF'ye dönüştürme - com.aspose.cells.CellsException: Geçersiz veri!|İstisna|
|CELLSJAVA-43112|PDF'ye dönüştürme - java.lang.NullPointerException|İstisna|
|CELLSJAVA-43115|PDF'ye dönüştürme - java.lang.NegativeArraySizeException|İstisna|
|CELLSJAVA-43116|PDF'ye dönüştürme - java.lang.IllegalStateException: Yapılandırılmış depolama bozuk görünüyor.|İstisna|
|CELLSJAVA-43120|çalışma kitabını PDF'ye dönüştürürken java.lang.NumberFormatException|İstisna|
### **Herkese Açık API ve Geriye Dönük Uyumsuz Değişiklikler**
Aşağıda, eklenen, yeniden adlandırılan, kaldırılan veya kullanımdan kaldırılan üyeler gibi genel API'de yapılan tüm değişikliklerin yanı sıra Java aracılığıyla PHP için Aspose.Cells'de yapılan geriye dönük uyumlu olmayan değişikliklerin bir listesi bulunmaktadır. Listelenen herhangi bir değişiklikle ilgili endişeleriniz varsa, lütfen Aspose.Cells destek forumunda yükseltin.
#### **FormulaParseOptions.Parse özelliğini ekler.**
Bir formül ifadesini hücreye ayarlarken formülün ayrıştırılıp ayrıştırılmayacağını gösterir. Varsayılan değer doğrudur. false ise, kullanıcı bunları ayrıştırmak için diğer yöntemleri çağırana veya formül hesaplama gibi diğer işlemler için ayrıştırılmış formül verileri gerekli olana kadar, giriş formülü ifadesi hücre için olduğu gibi tutulur.
#### **Workbook.ParseFormulas(bool ignoreError) yöntemini ekler.**
Yüklendiklerinde veya bir hücreye ayarlandıklarında ayrıştırılmamış tüm formülleri ayrıştırır.
#### **PivotTable.ExternalConnectionDataSource özelliğini ekler.**
Dış bağlantı veri kaynağını alır.
#### **FileFormatType.Numbers35 numaralandırmasını ekler.**
Office 2014'ten bu yana Number 3.5 dosyalarını temsil eder. Sadece okurken dosya formatını atmak içindir.
#### **LoadOptions.CheckDataValid özelliğini ekler.**
Dosyaları yüklerken geçersiz verilerin kontrol edilip edilmeyeceğini belirtir.

