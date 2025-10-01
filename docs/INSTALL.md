# ИНСТРУКЦИИ ПО УСТАНОВКЕ

## Системные требования
- Python 3.8+
- 8GB RAM (рекомендуется)
- 2GB свободного места

## Установка
```bash
# Клонировать репозиторий
git clone https://github.com/[username]/optical-connectome-analysis.git
cd optical-connectome-analysis

# Создать виртуальное окружение
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows

# Установить зависимости
pip install -r requirements.txt
```

## Использование
```bash
# Основной анализ
python scripts/optical_connectome_pipeline.py

# Создание графиков
python scripts/create_publication_figures.py

# Статистический анализ
python scripts/enhanced_statistics.py
```

## Данные
Данные находятся в папке `data/`:
- `ds006181_fixed_metrics.csv` - основные метрики
- `multi_dataset_optical_metrics.csv` - мультидатасетный анализ

## Результаты
Графики сохраняются в папку `figures/`:
- `Figure1_Distributions.png` - распределения
- `Figure2_Correlations.png` - корреляции
- `Figure3_3D_Tracts.png` - 3D тракты
- `Figure4_Network.png` - сеть
- `Figure5_Dataset_Comparison.png` - сравнение датасетов
- `ROC_Analysis.png` - ROC анализ

## Поддержка
При возникновении проблем создайте Issue в репозитории.
