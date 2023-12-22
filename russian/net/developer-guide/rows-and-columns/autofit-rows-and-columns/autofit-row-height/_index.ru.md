---
title: Автоматическая подгонка высоты строки при загрузке файла
type: docs
weight: 120
url: /ru/net/autofit-row-height/
description: Узнайте, как разместить строки, высота которых не настроена.
keywords: AutoFit Row Height when loading file, automatically adjust the row height when opening excel file. 
---
##  **Возможные сценарии использования**
 Высота строки автоматически соответствует шрифту содержимого, но если высота кэшированной строки не соответствует высоте содержимого в файле, MS Excel автоматически отрегулирует высоту строки при загрузке файла, а Aspose.Cells — нет. автоматически настройте его для улучшения производительности. Если вам необходимо использовать программу Aspose.Cells для автоматического сопоставления высоты строк при загрузке файлов, то добиться цели можно через параметр[LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/).

Пожалуйста, обратитесь к следующим данным изображения. Мы видим, что высота строки кэша в строке 11 равна 15, но Excel автоматически корректирует высоту строки при загрузке файла.
<br>
<img src="1.png" width=70% />

##  **Отрегулируйте высоту строки, используя Aspose.Cells.**
Если вы напрямую загрузите файл и сохраните его по адресу PDF, данные не будут полностью отображены по адресу PDF, поскольку высота строки его кэша составляет всего 15.
<br>
<img src="2.png" width=70% />
<br>
 Если вы установите параметр[LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/) значение true при загрузке файла, тогда Aspose.Cells автоматически отрегулирует высоту строки. Отрегулированная высота строки может эффективно удовлетворить требования к отображению текста.
<br>
<img src="3.png" width=70% />

##  **C# Пример кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rows-autofit-row-height.cs" >}}