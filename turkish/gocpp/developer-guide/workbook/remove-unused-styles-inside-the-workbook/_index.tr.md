---  
title: Golang kullanarak C++ ile Çalışma Kitabının içinde kullanılmayan stilleri kaldırın.  
linktitle: Çalışma Kitabı İçinde Kullanılmayan Stilleri Kaldırma  
type: docs  
weight: 340  
url: /tr/go-cpp/remove-unused-styles-inside-the-workbook/  
description: Golang kullanarak C++ ile Aspose.Cells ile Excel çalışma kitabındaki kullanılmayan stilleri kaldırın.  
---  

{{% alert color="primary" %}}  

Excel dosyalarındaki kullanılmayan stiller sadece yer kaplamaz, aynı zamanda PDF, HTML vb. farklı formatlara dönüştürürken performans sorunlarına da neden olur. Aspose.Cells, çalışma kitabındaki tüm kullanılmayan stilleri kaldırmanızı sağlayan [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/go-cpp/workbook/removeunusedstyles/) sağlar.  

{{% /alert %}}  

Aşağıdaki kod, [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/go-cpp/workbook/removeunusedstyles/) kullanımını açıklar. Kod, sağlanan bağlantıdan indirilebilecek şablon Excel dosyasını yükler. Bu dosyada **AsposeStyle** adlı kullanılmayan bir stil bulunmaktadır; bu stil ve diğer tüm kullanılmayan stiller, kod yürütüldükten sonra kaldırılacaktır.  

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)  

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemoveUnusedStylesInsideTheWorkbook.go" >}}
