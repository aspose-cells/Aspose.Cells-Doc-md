---
title: Почему не автоматизация
type: docs
weight: 20
url: /ru/java/why-not-automation/
---

{{% alert color="primary" %}}

Почему компоненты Aspose гораздо лучший вариант, чем автоматизация Microsoft Office?

Есть два вопроса, которые мы чаще всего слышим здесь в Aspose:

1. **Требуется ли установленный Microsoft Office для работы ваших продуктов?** 
   Простой ответ - нет. Компоненты Aspose полностью независимы и не являются ассоциированными, лицензированными, спонсированными или иным образом одобренными корпорацией Майкрософт.
1. **Почему мы должны использовать продукты Aspose вместо использования автоматизации Microsoft Office?**
   Самый краткий ответ, который мы можем дать, заключается в том, что есть много причин, основной из которых заключается в том, что сама Майкрософт настоятельно не рекомендует использовать автоматизацию Office из программных решений: [Рассмотрение возможностей серверной автоматизации Office](https://support.microsoft.com/en-us/topic/considerations-for-server-side-automation-of-office-48bcfe93-8a89-47f1-0bce-017433ad79e2).

Есть несколько причин, почему компоненты Aspose являются лучшей альтернативой для автоматизации. Некоторые из ключевых причин:

- [Безопасность](/cells/ru/java/why-not-automation/#security)
- [Стабильность](/cells/ru/java/why-not-automation/#security)
- [Масштабируемость/Скорость](/cells/ru/java/why-not-automation/#security)
- [Цена](/cells/ru/java/why-not-automation/#security)
- [Функции](/cells/ru/java/why-not-automation/#security)

Ключевые моменты описаны ниже. Также обязательно посетите ссылки в конце этого раздела.

{{% /alert %}}

## **Безопасность**

Нижеприведенная цитата напрямую из упомянутой выше статьи Майкрософт: *"Приложения Office никогда не предназначались для использования на стороне сервера и поэтому не учитывают проблемы безопасности, с которыми сталкиваются распределенные компоненты. Office не аутентифицирует входящие запросы и не защищает вас от непреднамеренного запуска макросов или запуска другого сервера, который может запустить макросы, с вашего серверного кода. Не открывайте файлы, загруженные на сервер из анонимной веб-страницы! На основе последних установленных настроек безопасности сервер может запускать макросы от имени администратора или системы с полными привилегиями и компрометировать вашу сеть! Кроме того, в Office используются многие компоненты на стороне клиента (такие как Simple MAPI, WinInet и MSDAIPP), которые могут кешировать информацию об аутентификации клиента для ускорения обработки. Если Office автоматизируется на стороне сервера, один экземпляр может обслуживать более одного клиента, и поскольку информация об аутентификации была кэширована для этой сессии, возможно, что один клиент может использовать закэшированные учетные данные другого клиента и таким образом получать разрешения на доступ, не предоставленные путем выдачи разрешения другим пользователям."*

Продукты Aspose очень безопасны. Компоненты Aspose работают в том же контексте пользователя, что и все приложения ASP.NET, под пользователем ASPNET. Поэтому компоненты Aspose не представляют потенциальной угрозы для важных системных ресурсов. Кроме того, когда документ открывается компонентом Aspose, макросы автоматически не запускаются. Компоненты Aspose были созданы с целью позволить разработчикам создавать, изменять и сохранять файлы Office. Ни один из рисков, связанных с пакетом Microsoft Office, не является присущим компонентам Aspose.

## **Стабильность**

Следующий прямая цитата из вышеупомянутой статьи Microsoft: "Office 2000, Office XP и Office 2003 используют технологию установщика Microsoft Windows (MSI), чтобы упростить установку и самовосстановление для конечного пользователя. MSI вводит концепцию "установки при первом использовании", которая позволяет функциям динамически устанавливаться или настраиваться во время выполнения (для системы или, чаще всего, для конкретного пользователя). В среде сервера это как замедляет производительность, так и увеличивает вероятность появления диалогового окна, запрашивающего у пользователя одобрение установки или предоставление соответствующего диска установки. Хотя это предназначено для повышения устойчивости Office в качестве продукта для конечного пользователя, использование возможностей MSI Office нерационально в среде сервера. Более того, устойчивость Office в общем нельзя обеспечить при запуске на стороне сервера, потому что он не был разработан или протестирован для такого типа использования. Если вы планируете автоматизировать Office на сервере, попытайтесь изолировать программу на выделенном компьютере, который не может влиять на критические функции, и который может быть перезапущен при необходимости."

Поскольку компоненты Aspose упакованы в один DLL, никогда не понадобится устанавливать какие-либо дополнительные части или элементы для их функционирования. Компоненты Aspose используются только в .NET-приложениях, и нет никакой части кода компонента, предназначенной для ожидания ответа человека. Компоненты Aspose были тщательно протестированы. Компоненты Aspose используются такими компаниями, как IBM, Hilton, Reader's Digest, Bank of America и многими другими.

## **Масштабируемость/Скорость**

Следующее прямая цитата из вышеупомянутой статьи Microsoft: "Компоненты на стороне сервера должны быть высоко повторяемыми, многопоточными COM-компонентами с минимальными накладными расходами и высокой пропускной способностью для нескольких клиентов. По всем практическим признакам приложения Office являются противоположностью этому. Они не повторяемы, базируются на STA (Single-Threaded Apartment) Automation серверах, предназначенных для предоставления разнообразной, но ресурсоемкой функциональности для одного клиента. Они предлагают небольшую масштабируемость в качестве решения на стороне сервера и имеют фиксированные пределы для важных элементов, таких как память, которые нельзя изменить через конфигурацию. Более того, они используют глобальные ресурсы (такие как файлы, размещенные в памяти, глобальные надстрои или шаблоны, и общие серверы Automation), которые могут ограничивать количество экземпляров, которые могут работать параллельно, и приводить к гонкам при условиях множественного клиента. Разработчики, планирующие запускать более одного экземпляра любого приложения Office одновременно, должны учитывать "пулинг" или последовательный доступ к приложению Office, чтобы избежать потенциальных взаимных блокировок или повреждения данных."

Компоненты Aspose обладают высокой масштабируемостью и моментальной скоростью. Приложения Office не были предназначены для одновременного использования сотнями и тысячами пользователей, однако компоненты Aspose разработаны именно на это. Наши компоненты - это истинное .NET решение и функционируют безупречно, будь то на одном сервере, обслуживающем одно приложение, или на сбалансированной нагрузке веб-фермы, обеспечивающей приложение на уровне предприятия.

## **Цена**

Когда приложение использует автоматизацию Microsoft Office, для каждого компьютера, на котором запускается приложение, должна быть куплена копия Microsoft Office. Очень часто приложению может потребоваться создание или изменение файла Office, но не требуется, чтобы пользователь имел Office. Aspose предлагает очень [эффективную по стоимости](https://purchase.aspose.com/buy), лицензию на свободное распространение, которая позволит развертывать приложения для неограниченного числа пользователей без забот о лицензировании.

При создании веб-приложений важно знать, что компоненты автоматизации Microsoft Office не имеют цены и лицензии для решений на стороне сервера; следовательно, нет хорошего, лицензионного решения для развертывания веб-приложений, использующих компоненты Microsoft Office. Aspose предлагает очень эффективное решение для серверных приложений также.

## **Функции**

Компоненты Aspose предоставляют все необходимое для управления файлами Office, плюс многое другое. Они разработаны с философией позволяющей разработчикам достигать наилучших результатов с минимальными усилиями. В отличие от автоматизации Office, компоненты Aspose предоставляют множество мощных, экономящих время функций. Например, [Aspose.Cells](https://products.aspose.com/cells/java/) предлагает разработчикам возможность экспортировать из **DataTable** или **DataView** непосредственно в файл Excel. *Each component* в семействе Aspose предлагает свой собственный набор уникальных, мощных функций.

Лучшая часть приобретения компонента Aspose или комплекта компонентов - это возможность общения с нашими командами разработчиков. Наша группа разработчиков понимает, что если у вашей компании есть функция, вероятно, ее потребуется и другим компаниям. Хотя не все запросы на добавление функций могут быть удовлетворены, наши команды стараются быть очень открытыми и гибкими при предоставлении помощи. Именно такое мышление помогло компонентам Aspose стать такими мощными. Есть очень маленькая вероятность, что дополнительные функции, которые вам нужны от объектов автоматизации Office, будут добавлены.

## **Заключение**

{{% alert color="primary" %}}

В этой статье были рассмотрены основные причины, почему компоненты Aspose являются более предпочтительным выбором, чем автоматизация Office. Все различные компоненты Aspose предлагают версию для [оценки без риска и обязательств](https://products.aspose.com/total/). Мы призываем вас воспользоваться этой оценкой, чтобы лучше узнать, что может сделать Aspose для ваших приложений.

Дополнительные статьи по этой теме можно прочитать в сети Интернет:

- [Соображения при автоматизации на стороне сервера Office](https://support.microsoft.com/en-us/topic/considerations-for-server-side-automation-of-office-48bcfe93-8a89-47f1-0bce-017433ad79e2)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
