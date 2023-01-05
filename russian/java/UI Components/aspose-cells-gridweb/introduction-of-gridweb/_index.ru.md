---
title: Введение GridWeb
type: docs
weight: 10
url: /ru/java/introduction-of-gridweb/
---
## **Как запустить Aspose.Cells для демонстрации GridWeb Java**
{{% alert color="primary" %}} 

 Aspose.Cells для демонстрационных версий GridWeb Java легко запустить. Вам просто нужно развернуть**gridwebdemo.war** на вашем веб-сервере. Пожалуйста, загрузите демо отсюда[соединять](https://forum.aspose.com/uploads/discourse_instance3/22292).

В этой статье описывается, как запустить Aspose.Cells для демонстрации GridWeb Java на сервере Apache Tomcat.

{{% /alert %}} 
### **Пошаговое руководство по запуску демонстраций GridWeb Java**
1.  Извлекать**apache-tomcat-7.0.52.zip** в любом каталоге, например, C:\Tomcat

![дело:изображение_альтернативный_текст](introduction-of-gridweb_1.png)



 На следующем снимке показаны извлеченные каталоги и файлы сервера Apache Tomcat.

![дело:изображение_альтернативный_текст](introduction-of-gridweb_2.png)



 Вам также может потребоваться установить переменную среды**CATALINA_HOME** 

![дело:изображение_альтернативный_текст](introduction-of-gridweb_3.png)

1. Открыть**tomcat-users.xml** файл.

![дело:изображение_альтернативный_текст](introduction-of-gridweb_4.png)

1. Добавьте этого пользователя:

{{< highlight "java" >}}

   <role rolename="manager-gui"/>

  <user username="tomcat" password="secret" roles="manager-gui"/>

{{< /highlight >}}



**Здесь имя пользователя tomcat и секретный пароль** 

![дело:изображение_альтернативный_текст](introduction-of-gridweb_5.png)

1.  Запустите**запуск.bat** файл.
 Он будет запускать сервер Apache Tomcat.

![дело:изображение_альтернативный_текст](introduction-of-gridweb_6.png)



**Сервер Tomcat работает в командном окне** 

![дело:изображение_альтернативный_текст](introduction-of-gridweb_7.png)

1.  Теперь откройте браузер и введите**локальный: 8080**.
 Отображается веб-страница Apache Tomcat.

   **Веб-страница Apache Tomcat** 

![дело:изображение_альтернативный_текст](introduction-of-gridweb_8.png)

1.  Нажмите**Приложение менеджера** и введите имя пользователя и пароль. (Как указано выше: кот, секрет)

![дело:изображение_альтернативный_текст](introduction-of-gridweb_9.png)

1.  Прокрутите вниз до раздела**WAR-файл для развертывания** и просмотрите**gridwebdemo.war** файл.
1.  Нажмите**Развертывать**. 

![дело:изображение_альтернативный_текст](introduction-of-gridweb_10.png)

1.  Просматривать**gridwebdemo.war** файл.

![дело:изображение_альтернативный_текст](introduction-of-gridweb_11.png)

1.  Нажмите**Развертывать**. 

![дело:изображение_альтернативный_текст](introduction-of-gridweb_12.png)

1.  После развертывания нажмите**/gridwebdemo** и запустить демоверсии.

![дело:изображение_альтернативный_текст](introduction-of-gridweb_13.png)


 Отображается демонстрационная страница GridWeb.

**Демонстрационная страница GridWeb** 

![дело:изображение_альтернативный_текст](introduction-of-gridweb_14.png)

1.  Щелкните любое демо и запустите его.

   **Работает демонстрация создания содержимого** 

![дело:изображение_альтернативный_текст](introduction-of-gridweb_15.png)



**Работает демонстрация рабочих листов** 

![дело:изображение_альтернативный_текст](introduction-of-gridweb_16.png)



**Работает демонстрация HeaderBar и CommandButton** 

![дело:изображение_альтернативный_текст](introduction-of-gridweb_17.png)
## **Aspose.Cells.GridWeb — Демонстрации**
{{% alert color="primary" %}} 

Чтобы вы могли быстро приступить к работе, мы предоставляем ряд примеров кода и демонстраций, которые показывают, как использовать Aspose.Cells.GridWeb API.

Пожалуйста, загрузите демоверсии по ссылке ниже:
[Aspose.Cells. Демонстрации GridWeb](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb)

{{% /alert %}} 
## **Возможности браузеров и Aspose.Cells.GridWeb**
Aspose.Cells.GridWeb — это веб-элемент управления на основе графического интерфейса, который можно встраивать в веб-страницы JSP, как и другие веб-элементы управления. Самая важная вещь в веб-контроле — обеспечение кросс-браузерной поддержки. Aspose.Cells.GridWeb обеспечивает кроссбраузерную поддержку.
### **Сравнение**
Aspose.Cells.GridWeb полностью поддерживается в Internet Explorer (IE) Microsoft. Однако в других браузерах он имеет небольшие ограничения. В этом разделе представлено подробное сравнение функций, поддерживаемых разными браузерами.

|**Функции на стороне клиента**|**Microsoft Internet Explorer**|**Google Хром**|**Мозилла Фаерфокс**|**Опера**|
|:- |:- |:- |:- |:- |
|Контекстное меню Cell|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/cross >}}|
|Проверка на стороне клиента|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Событие двойного щелчка|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| Выпадающий список (*Режим со списком* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| Выпадающий список (*Режим всплывающего меню* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Ввод/редактирование формулы|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Заморозить или разморозить строки/столбцы|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| Гиперссылки (*Режим CellCommand* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| Гиперссылки (*Режим URL* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Объединить или разъединить Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Несколько Cells Копировать/Вставить|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Множественный ввод/редактирование Cells, одиночная обратная передача|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Формат номера|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Пейджинг листа|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Только для чтения Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Строки/столбцы только для чтения|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Проверка данных с использованием регулярных выражений|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Изменить ширину столбца|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Изменить высоту строки|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Вставка/удаление строк и столбцов|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Прокрутить содержимое|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Вкладки листа прокрутки|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Установить границы Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Установите настройки шрифта Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
{{< emoticons/cross >}} Контекстное меню ячейки можно активировать только нажатием кнопки меню на стороне клиента.
