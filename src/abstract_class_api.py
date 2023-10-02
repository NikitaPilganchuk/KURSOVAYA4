from abc import ABC, abstractmethod
class AbstractClassAPI(ABC):
    '''
    Абстрактный клосс для работы с API сайтов
    '''
    @abstractmethod
    def get_vacancies(self):
        pass
