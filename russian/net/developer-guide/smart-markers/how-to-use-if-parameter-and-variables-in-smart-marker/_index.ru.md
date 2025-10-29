---
title: Как использовать условие if и переменные в SmartMarkers
type: docs
weight: 10
url: /ru/net/how-to-use-if-parameter-and-Variables-in-smart-markers/
---

## **Почему стоит использовать условие if и переменные в Smart Markers**
Smart Markers — мощные инструменты, используемые в различных контекстах. Использование параметров и переменных внутри Smart Markers значительно повышает их гибкость, эффективность и функциональность.

1. Динамическая обработка данных и гибкость: параметры и переменные позволяют Smart Markers динамически управлять данными, адаптируясь к меняющимся входным данным без необходимости ручных настроек шаблона или кода.
2. Контроль поведения и операций: параметры тонко настраивают поведение Smart Markers, позволяя выполнять такие операции, как группировка, сортировка, подсчет итогов и условное форматирование.
3. Поддержка сложных структур данных: переменные позволяют Smart Markers работать с сложными источниками данных, включая массивы, объекты и многомерные данные.
4. Эффективность и автоматизация: параметры и переменные автоматизируют повторяющиеся задачи, уменьшая ручные усилия и возможные ошибки.
5. Условная логика и фильтрация: хотя в некоторых контекстах их ограниченность, параметры и переменные могут реализовать условную логику.
6. Настройка и взаимодействие с пользователем: переменные позволяют пользователю вводить данные для динамической настройки поведения Smart Marker.
7. Оптимизация производительности: параметры помогают оптимизировать производительность, контролируя обработку данных.


## **Как использовать условие if и переменные в SmartMarkers**
Иногда необходимо добавить условие if к параметрам переменных в SmartMarkers. Aspose.Cells позволяет использовать условие if и переменные в SmartMarkers. Пожалуйста, ознакомьтесь с [шаблонным файлом](template.xlsx), [json файлом](data.json) и скриншотом сгенерированного выходного файла Excel с помощью следующего кода.

|**Первая рабочая таблица файла template.xlsx показывает переменные.**|
| :- |
|![todo:image_alt_text](variables.png)|

|**Вторая рабочая таблица файла template.xlsx показывает smart маркеры.**|
| :- |
|![todo:image_alt_text](template.png)|

|**Скриншот выходного файла Excel.**|
| :- |
|![todo:image_alt_text](result.png)|

Следующие данные JSON:
```json data
{
    "Directors": [
        {
            "FirstName": "director first 1",
            "id": "director id 1",
            "LastName": "director last 1",
            "MiddleName": "director middle 1",
            "Reportees": [
                {
                    "City": "aaa city",
                    "Department": "aaa department",
                    "FirstName": "first aaa",
                    "GST": "Yes",
                    "id": "aaa",
                    "ITR": "No",
                    "LastName": "last aaa",
                    "MiddleName": "middle aaa"
                },
                {
                    "City": "bbb city",
                    "Department": "bbb department",
                    "FirstName": "first bbb",
                    "GST": "Yes",
                    "id": "bbb",
                    "ITR": "Yes",
                    "LastName": "last bbb",
                    "MiddleName": "middle bbb"
                },
                {
                    "City": "ccc city",
                    "Department": "ccc department",
                    "FirstName": "first ccc",
                    "GST": "No",
                    "id": "ccc",
                    "ITR": "No",
                    "LastName": "last ccc",
                    "MiddleName": "middle ccc"
                }
            ]
        },
        {
            "FirstName": "director first 2",
            "id": "director id 2",
            "LastName": "director last 2",
            "MiddleName": "director middle 2",
            "Reportees": [
                {
                    "City": "eee city",
                    "Department": "eee department",
                    "FirstName": "first eee",
                    "GST": "Yes",
                    "id": "eee",
                    "ITR": "No",
                    "LastName": "last eee",
                    "MiddleName": "middle eee"
                },
                {
                    "City": "fff city",
                    "Department": "fff department",
                    "FirstName": "first fff",
                    "GST": "No",
                    "id": "fff",
                    "ITR": "No",
                    "LastName": "last fff",
                    "MiddleName": "middle fff"
                }
            ]
        }
    ],
    "DOB": "2025-02-08",
    "EntityCin": "EntityCin Test",
    "EntityName": "EntityName Test",
    "FirstName": "FirstName Test",
    "LastName": "LastName Test",
    "MiddleName": "MiddleName Test",
    "SSN": "11111111"
}
```
Приведенный ниже пример показывает, как это работает.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-If-Parameter-And-Variables.cs" >}}

{{< app/cells/assistant language="csharp" >}}
