---  
title: Создать общую рабочую книгу с помощью Aspose.Cells и Golang через C++  
linktitle: Создание общей книги с Aspose.Cells  
type: docs  
weight: 40  
url: /ru/go-cpp/create-shared-workbook-with-aspose-cells/  
description: Узнайте, как создать общую рабочую книгу с помощью Aspose.Cells и Golang через C++  
---  

## **Возможные сценарии использования**  

Microsoft Excel позволяет делиться книгой, как показано на следующем скриншоте. Когда вы делитесь рабочей книгой, более одного пользователя могут ее редактировать в сети. Aspose.Cells позволяет создавать совместную книгу с помощью свойства [**Workbook.GetShared()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getshared/).  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)  

## **Создание общей книги с Aspose.Cells**  

Следующий пример кода создает совместную книгу, устанавливая свойство [**Workbook.GetShared()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getshared/) в значение **true**. Открыв [выходной файл Excel](55541786.xlsx) в Microsoft Excel, вы увидите указание **Shared** рядом с именем файла, как показано на скриншоте.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)  

## **Образец кода**  

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreateSharedWorkbookWithAsposeCells.go" >}}
