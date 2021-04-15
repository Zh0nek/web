def make_out_word(out, word):
  out_1 = out[:len(out)/2]
  out_2 = out[len(out)/2:len(out)]
  return out_1 + word + out_2
