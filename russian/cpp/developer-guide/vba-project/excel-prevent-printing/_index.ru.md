---  
title: Как предотвратить печать файла Excel пользователями с помощью C++  
linktitle: Как предотвратить пользователей от печати файлов Excel  
type: docs  
weight: 600  
url: /ru/cpp/how-to-prevent-printing-excel/  
description: Узнайте, как предотвратить печать Excel через API Aspose.Cells for C++.  
keywords: печать excel, предотвращение печати excel, как предотвратить пользователей от печати excel, excel предотвращение печати, предотвращение печати рабочей книги, Предотвращение печати всей книги с помощью VBA.  
---  

## **Возможные сценарии использования**  
В нашей ежедневной работе в файле Excel может содержаться важная информация; чтобы защитить внутренние данные от распространения, компания не разрешит их печать. Этот документ расскажет, как предотвратить печать файлов Excel другими.  

## **Как предотвратить пользователей от печати файла в MS-Excel**  
Вы можете применить следующий VBA-код для защиты вашего конкретного файла от печати.  
1. Откройте свою книгу, которую вы не разрешаете печатать.  
1. Выберите вкладку "Developer" на ленте Excel и нажмите кнопку "View Code" в разделе "Controls". Или удерживайте клавиши ALT + F11 для открытия окна Microsoft Visual Basic for Applications.  
<br>  
<img src="1.png" width=70% />  
1. Затем в левом окне Project Explorer дважды щелкните ThisWorkbook, чтобы открыть модуль, и добавьте некоторые VBA-коды.  
<br>  
<img src="2.png" width=70% />  
1. Затем сохраните и закройте этот код, вернитесь в рабочую книгу, и теперь при попытке распечатать файл образца выводится предупреждение:  
<br>  
<img src="3.png" width=70% />  

## **Как запретить пользователям печатать файл Excel с помощью Aspose.Cells for C++**  

Следующий пример кода показывает, как предотвратить печать файла Excel:  

1. Загрузите [образец файла](sample.xlsx).  
1. Получите объект VbaModuleCollection через свойство VbaProject книги.  
1. Получите объект VbaModule через имя "ThisWorkbook".  
1. Установите свойство codes объекта VbaModule.  
1. Сохраните образец файла в формате [xlsm](out.xlsm).  

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
