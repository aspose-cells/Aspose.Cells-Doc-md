---
title: Введение GridWeb
type: docs
weight: 10
url: /ru/java/introduction-of-gridweb/
---
##  **Основы GridWeb**
 Aspose.Cells.GridWeb — это веб-элемент управления на основе графического пользовательского интерфейса, который можно встроить в веб-страницы JSP или любую HTML-страницу на Java-сервере.
{{% alert color="primary" %}} 

Его легко и просто использовать.

Он поможет вам быстро создать онлайн-веб-редактор для файлов электронных таблиц.

Он также поддерживает импорт и экспорт всех видов файлов формата электронных таблиц, которые на 100% совместимы с файлами MS Excel.

##  **Aspose.Cells.GridWeb — Демоверсии**
{{% alert color="primary" %}} 

Чтобы вы могли быстро приступить к работе, мы предоставляем ряд примеров кода и демонстраций, которые показывают, как использовать Aspose.Cells.GridWeb API.

Загрузите демо-версии по ссылке ниже:
[Aspose.Cells.Демоверсии GridWeb](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb)


##  **Как запустить Aspose.Cells для GridWeb Java Демоверсии**
{{% alert color="primary" %}} 

 Aspose.Cells для GridWeb Java Демоверсии легко запустить. Вам просто нужно развернуть**Gridwebdemo.war** на вашем веб-сервере. Пожалуйста, загрузите демо-версии отсюда[связь](https://forum.aspose.com/uploads/discourse_instance3/22292).

В этой статье описывается, как запустить Aspose.Cells для демонстрационных версий GridWeb Java на сервере Apache Tomcat.

{{% /alert %}} 
###  **Пошаговое руководство по запуску демонстраций GridWeb Java**
1.  Извлекать**apache-tomcat-7.0.52.zip** в любом каталоге, например C:\Tomcat

![задача: image_alt_text](introduction-of-gridweb_1.png)



 На следующем снимке показаны извлеченные каталоги и файлы сервера Apache Tomcat.

![задача: image_alt_text](introduction-of-gridweb_2.png)



 Вам также может потребоваться установить переменную среды**CATALINA_HOME** 

![задача: image_alt_text](introduction-of-gridweb_3.png)

1.  Открой**tomcat-users.xml** файл.

![задача: image_alt_text](introduction-of-gridweb_4.png)

1. Добавьте этого пользователя:

{{< highlight "java" >}}

   <role rolename="manager-gui"/>

  <user username="tomcat" password="secret" roles="manager-gui"/>

{{< /highlight >}}



**Здесь имя пользователя — tomcat, а пароль — секретный.** 

![задача: image_alt_text](introduction-of-gridweb_5.png)

1.  Запустите**start.bat** файл.
 Он будет запускать сервер Apache Tomcat.

![задача: image_alt_text](introduction-of-gridweb_6.png)



**Сервер Tomcat, работающий в командном окне** 

![задача: image_alt_text](introduction-of-gridweb_7.png)

1. Теперь откройте браузер и введите *localhost:8080**.
 Откроется веб-страница Apache Tomcat.

   **Веб-страница Apache Tomcat** 

![задача: image_alt_text](introduction-of-gridweb_8.png)

1.  Нажмите**Приложение Менеджер** и введите имя пользователя и пароль. (Как указано выше: кот, секрет)

![задача: image_alt_text](introduction-of-gridweb_9.png)

1.  Прокрутите вниз до раздела**WAR-файл для развертывания** и просмотрите**Gridwebdemo.war** файл.
1.  Нажмите *Развернуть**.

![задача: image_alt_text](introduction-of-gridweb_10.png)

1. Просматривать**Gridwebdemo.war** файл.

![задача: image_alt_text](introduction-of-gridweb_11.png)

1.  Нажмите *Развернуть**.

![задача: image_alt_text](introduction-of-gridweb_12.png)

1.  После развертывания нажмите**/gridwebdemo** и начните запускать демоверсии.

![задача: image_alt_text](introduction-of-gridweb_13.png)


 Откроется демонстрационная страница GridWeb.

**Демо-страница GridWeb** 

![задача: image_alt_text](introduction-of-gridweb_14.png)

1.  Нажмите на любую демо-версию и запустите ее.

   **Создание демо-версии содержимого** 

![задача: image_alt_text](introduction-of-gridweb_15.png)



**Демо-версия рабочих листов** 

![задача: image_alt_text](introduction-of-gridweb_16.png)



**Демо-версия HeaderBar и CommandButton запущена** 

![задача: image_alt_text](introduction-of-gridweb_17.png)


{{% /alert %}} 
##  **Возможности браузеров и Aspose.Cells.GridWeb**
Aspose.Cells.GridWeb — это веб-элемент управления на основе графического пользовательского интерфейса, который можно встраивать в веб-страницы JSP, как и другие веб-элементы управления. Самое важное в веб-контроле — обеспечение кроссбраузерной поддержки. Aspose.Cells.GridWeb обеспечивает кросс-браузерную поддержку.
###  **Сравнение**
Aspose.Cells.GridWeb полностью поддерживается в Internet Explorer (IE) Microsoft. Однако в других браузерах он имеет незначительные ограничения. В этом разделе представлено подробное сравнение функций, поддерживаемых различными браузерами.

|**Возможности клиентской стороны**|**Microsoft Интернет Эксплорер**|**Google Хром**|**Мозилла Фаерфокс**|**Опера**|
| :- | :- | :- | :- | :- |
|Контекстное меню Cell|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/cross >}}|
|Проверка на стороне клиента|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Событие двойного щелчка|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| Выпадающий список (*Режим ComboBox* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| Выпадающий список (*Режим всплывающего меню* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Ввод/редактирование формулы|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Закрепить или разморозить строки/столбцы|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| Гиперссылки (*Режим CellCommand* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| Гиперссылки (*URL-режим* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Объединить или разъединить Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Несколько Cells Копировать/Вставить|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Множественный ввод/редактирование Cells, одиночная обратная передача|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Числовой формат|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Перелистывание листов|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Только чтение Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Строки/столбцы только для чтения|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Проверка данных с использованием регулярных выражений|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Изменение размера ширины столбца|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Изменить размер строки|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Вставка/удаление строк и столбцов|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Прокрутка содержимого|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Прокрутка вкладок листа|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Установить границы Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Установите настройки шрифта Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
{{< emoticons/cross >}} Контекстное меню ячейки можно активировать только нажатием кнопки Клиентское меню.
