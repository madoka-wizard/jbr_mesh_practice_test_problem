# Тестовое задание для весенней практики JetBrains «Разметка облаков точек и mesh для оценки геометрических характеристик объектов (JBR)»

Данное приложение на Python 3 служит для обработки аудио файлов. Решение удовлетворяет следующим требованиям:
- режим склеивания произвольного количества аудиофайлов в один;
- режим нарезки входного файла по списку интервалов;
- режим нарезки входного файла на куски по списку тайм-кодов;
- режим инвертирования входного файла;
- присутствует образ Docker.

# Установка
## Ручная установка
В системе должен быть установлен интерпретатор Python 3.9. Для работы с аудио файлами приложение использует библиотеку
[pydub](https://pydub.com) версии 0.25.0. Можно установить зависимости из requirements.txt или из Pipfile, если использовать [Pipenv](https://pipenv.pypa.io). Исполняемый файл находится в скрипте simple_audio_processor.py.

## Через Docker образ
TODO

# Использование
```
usage: simple_audio_processor.py [-h] COMMAND ...
```

Задавать имена файлов нужно вместе с раширением, например: `a.mp3`.
Поддерживаются любые форматы, которые поддерживает [FFmpeg](https://www.ffmpeg.org/general.html#File-Formats),
Если на системе установлен FFmpeg, то их можно посмотреть с помощью компанды `ffmpeg -formats`.

Список доступных операций с аудио файлами:
- Конкатенация произвольного количества аудио файлов (возможно с различными расширениями) в один:
```shell
usage: simple_audio_processor.py concat [-h] INPUT_FILE [INPUT_FILE ...] OUTPUT_FILE
```
- Вырезание из аудио файла произвольного числа интервалов (возможно пересекающихся). 
Список интервалы передается последним аргументом, указывающим на путь текстового файла,
содержащего по одному интервалу в каждой своей строке. Интервалы записываются в формате `START-END`,
где `START` и `END` — моменты времени с начала звуковой дорожки в формате `hh:mm:ss.SSS` или целое число
— количество миллисекунд с начала трека. На выходе получим набор файлов в директории,
из которой вызывался скрипт, соответствующий списку интервалов. К `i`-му файлу перед
расширением будет добавлен префикс `_i` (нумерация с 1).
```shell
simple_audio_processor.py cut [-h] INPUT_FILE INTERVALS_FILE
```
- Разбиение входного файла на куски по тайм-кодам. Список тайм-кодов передается последним аргументом,
указывающим на путь текстового файла, содержащего по одному тайм-коду в каждой своей строке. Тайм-коды записываются
в формате `hh:mm:ss.SSS` или целое число — количество миллисекунд с начала трека. На выходе получим набор файлов в
директории, из которой вызывался скрипт, соответствующий списку тайм-кодов (списку из
`n` тайм-кодов соответствуют `n + 1` фрагментов). К `i`-му файлу перед
расширением будет добавлен префикс `_i` (нумерация с 1).
```shell
usage: simple_audio_processor.py ts [-h] INPUT_FILE TS_FILE
```
- Инвертирование входного файла. Опционально передается аргумент `---out` с именем
выходного файла (если опустить аргумент, то в качестве имени будет
взято исходное имя с префиксом `_reversed` перед расширением).
```shell
usage: simple_audio_processor.py reverse [-h] [--out OUTPUT_FILE] INPUT_FILE
```
