﻿---
title: Отключить проверку совместимости в Excel
type: docs
weight: 270
url: /ru/java/disable-compatibility-checker-in-excel/
---
{{% alert color="primary" %}}

Microsoft Средство проверки совместимости Excel помечает при сохранении файла в более раннем формате файла, что сохранение файла может вызвать проблемы с функциональностью или потерю точности. Средство проверки совместимости — это функция Microsoft Office Excel 2007, 2010 и 2013.

Когда вы сохраняете книгу в предыдущей версии, от Excel 97 до Excel 2003, из Excel 2007 или Excel 2010, средство проверки совместимости сканирует книгу, чтобы определить, содержит ли она функции, которые не поддерживаются в более ранней версии. Чтобы помочь вам принять решение о том, как справляться с проблемами совместимости, средство проверки совместимости отображает диалоговые окна с параметрами. Его также можно использовать для создания отчета о любых проблемах в книге или отключения этой функции.

Иногда вам нужно отключить средство проверки совместимости для определенной электронной таблицы. С помощью API-интерфейсов Aspose.Cells' вы можете делать это динамически, чтобы пользователи не расстраивались и не сбивались с толку из-за всплывающего диалогового окна средства проверки совместимости, когда они повторно сохраняют файл в Microsoft Excel вручную.

{{% /alert %}}

## **Использование Microsoft Excel**

Чтобы отключить средство проверки совместимости в Microsoft Excel (например, Microsoft Excel 2007/2010):

-  (Excel 2007) На кнопке Office щелкните**Подготовить** , тогда**Запустить проверку совместимости** , а затем очистите**Проверяйте совместимость при сохранении этой книги** вариант.
-  (Excel 2010 и 2013) На вкладке «Файл» щелкните**Информация** , тогда**Проверить наличие проблем** , нажмите**Проверить совместимость** , и, наконец, очистить**Проверяйте совместимость при сохранении этой книги** вариант.

## **Использование API Aspose.Cells**

 Установить[**WorkbookSettings.CheckComptiliblity**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckComptiliblity) собственность на**ЛОЖЬ** чтобы отключить Microsoft средство проверки совместимости Excel.

Предположим, у нас есть файл шаблона XLS. Когда пользователь сохраняет или повторно сохраняет его в MS Excel 2007/2010/2013, отображается диалоговое окно «Проверка совместимости», как показано на снимке экрана ниже.

![дело:изображение_альтернативный_текст](disable-compatibility-checker-in-excel_1.png)

В следующем коде показано, как отключить средство проверки совместимости с Aspose.Cells for Java.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableCompatibilityChecker-DisableCompatibilityChecker.java" >}}
