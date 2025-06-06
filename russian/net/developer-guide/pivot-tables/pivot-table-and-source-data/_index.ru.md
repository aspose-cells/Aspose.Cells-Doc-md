---
title: Сводная таблица и исходные данные
type: docs
weight: 30
url: /ru/net/pivot-table-and-source-data/
---

## **Исходные данные сводной таблицы**

Иногда возникают ситуации, когда вы хотите создать отчеты Microsoft Excel с сводными таблицами, использующими данные из разных источников данных (например, базы данных), которые неизвестны на этапе проектирования. В этой статье представлен подход к динамическому изменению источника данных сводной таблицы.

### **Изменение исходного источника данных сводной таблицы**

1. Создание нового файла шаблона дизайнера.
   1. Создайте новый файл шаблона дизайнера, как показано на скриншоте ниже.
   1. Затем определите именованный диапазон **DataSource**, который ссылается на этот диапазон ячеек.

      **Создание файла шаблона дизайнера и определение именованного диапазона DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_1.png)

1. Создание сводной таблицы на основе этого именованного диапазона.
   1. В Microsoft Excel выберите **Данные**, затем **Сводная таблица** и **Отчет сводной таблицы и диаграмма**.
   1. Создайте сводную таблицу на основе созданного в первом шаге именованного диапазона.

      **Создание сводной таблицы на основе именованного диапазона DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_2.png)


   1. Перетащите соответствующее поле на строку и столбец сводной таблицы, затем создайте результирующую сводную таблицу, как показано на скриншоте ниже.

   **Создание сводной таблицы на основе соответствующего поля** 

![todo:image_alt_text](pivot-table-and-source-data_3.png)


1. Щелкните правой кнопкой мыши на сводной таблице и выберите **Параметры таблицы**.
   1. Установите **Обновлять при открытии** в настройках **Параметры данных**.

      **Настройка параметров сводной таблицы** 

![todo:image_alt_text](pivot-table-and-source-data_4.png)


Теперь вы можете сохранить этот файл как файл вашего дизайнерского шаблона.

1. Пополнение новыми данными и изменение исходных данных сводной таблицы.
   1. После создания дизайнерского шаблона используйте следующий код для изменения исходных данных сводной таблицы.

Исполнение приведенного ниже примера кода изменяет исходные данные сводной таблицы.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ChangeSourceData-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
