from app import Elevador


def test_subir():
    elevador = Elevador()
    assert elevador.subir() == 2


def test_descer_no_primeiro_andar():
    elevador = Elevador()
    assert elevador.descer() == 1


def test_ir_para_andar_valido():
    elevador = Elevador()
    assert elevador.ir_para(6) == 6


def test_nao_ultrapassa_ultimo_andar():
    elevador = Elevador(6)
    assert elevador.subir() == 6


def test_nao_desce_abaixo_primeiro_andar():
    elevador = Elevador(1)
    assert elevador.descer() == 1
