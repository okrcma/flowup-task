import pytz
from datetime import datetime, timedelta


class Timer:
    def __init__(self, tid: str):
        self.tid = tid
        self._started_at: datetime | None = None
        self._stopped_at: datetime | None = None

    def start(self) -> None:
        if self._started_at is not None:
            raise Exception("Timer already started")
        self._started_at = datetime.now(pytz.UTC)

    def stop(self) -> None:
        if self._started_at is None:
            raise Exception("Timer was not started yet")
        if self._stopped_at is not None:
            raise Exception("Timer already stopped")
        self._stopped_at = datetime.now(pytz.UTC)

    def read(self) -> timedelta:
        if self._started_at is None:
            return timedelta()
        end_time = datetime.now(pytz.UTC) if self._stopped_at is None else self._stopped_at
        return end_time - self._started_at


class TimerRegistry:
    def __init__(self) -> None:
        self._timer_map: dict[str, Timer] = {}

    def register(self, timer: Timer) -> None:
        assert timer.tid not in self._timer_map
        self._timer_map[timer.tid] = timer

    def get(self, tid: str) -> Timer:
        return self._timer_map[tid]


timer_registry = TimerRegistry()
