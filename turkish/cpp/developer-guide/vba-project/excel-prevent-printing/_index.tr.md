---  
title: C++ ile Kullanıcıların Excel Dosyasını Yazdırmasını Nasıl Önlersiniz  
linktitle: Excel Dosyasının Yazdırılmasını Nasıl Engelleriz  
type: docs  
weight: 600  
url: /tr/cpp/how-to-prevent-printing-excel/  
description: Aspose.Cells for C++ API si aracılığıyla kullanıcıların Excel dosyasını yazdırmasını nasıl engelleyeceğinizi öğrenin.  
keywords: excel yazdırma, excel yazdırmayı engelleme, kullanıcıların excel i yazdırmaması nasıl engellenir, excel yazdırma engelleme, çalışma kitabının yazdırılmasını engelleme, Kullanıcıların VBA ile tam çalışma kitabını yazdırmalarını engelleyin.  
---  

## **Olası Kullanım Senaryoları**  
Günlük çalışmalarımızda, Excel dosyasında önemli bilgiler olabilir; iç verilerin yayılmasını önlemek için şirketimiz bunların yazdırılmasını engelleyecektir. Bu belge, başkalarının Excel dosyalarını yazdırmasını nasıl engelleyeceğinizi anlatacaktır.  

## **MS-Excel'de Kullanıcıların Dosyayı Yazdırmasını Nasıl Engelleriz**  
Aşağıdaki VBA kodunu kullanarak belirli dosyanızın yazdırılmasını engelleyebilirsiniz.  
1. Başkalarına yazdırmalarına izin vermediğiniz çalışma kitabınızı açın.  
1. Excel şeridinde "Geliştirici" sekmesini seçin ve "Kod Görüntüle" düğmesine tıklayın "Kontroller" bölümünde. Alternatif olarak, Microsoft Visual Basic for Applications penceresini açmak için ALT + F11 tuşlarını basılı tutabilirsiniz.  
<br>  
<img src="1.png" width=70% />  
1. Daha sonra sol Project Explorer'da ThisWorkbook üzerine çift tıklayarak modülü açın ve bazı VBA kodları ekleyin.  
<br>  
<img src="2.png" width=70% />  
1. Daha sonra bu kodu kaydedin ve kapatın, tekrar çalışma kitabına dönün ve şimdi örnek dosyayı yazdırmak istediğinizde, yazdırılamayacak ve aşağıdaki uyarı kutusunu alacaksınız:  
<br>  
<img src="3.png" width=70% />  

## **Aspose.Cells for C++ kullanarak Kullanıcıların Excel Dosyasını Yazdırmasını Nasıl Engellersiniz**  

Aşağıdaki örnek kod, kullanıcıların Excel dosyasını yazdırmasını nasıl engelleyeceğinizi gösterir:  

1. [Örnek dosyayı](örnek.xlsx) yükleyin.  
1. VbaProje özelliğinden VbaModuleCollection nesnesini alın.  
1. "ThisWorkbook" adıyla VbaModule nesnesini elde edin.  
1. VbaModule'nin kodları özelliğini ayarlayın.  
1. Örnek dosyayı [xlsm biçimine](out.xlsm) kaydedin.  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook from existing Excel file
    Workbook workbook(u"Sample.xlsx");

    // Access VBA project modules
    VbaModuleCollection modules = workbook.GetVbaProject().GetModules();

    // Set VBA code for 'ThisWorkbook' module
    modules.Get(u"ThisWorkbook").SetCodes(u"Private Sub Workbook_BeforePrint(Cancel As Boolean)\r\n  Cancel = True\r\n  MsgBox \"Refusing to print in paperless office\"\r\nEnd Sub\r\n");

    // Save the workbook as macro-enabled Excel file
    workbook.Save(u"out.xlsm");

    std::cout << "VBA code added and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  
